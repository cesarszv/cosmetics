from __future__ import annotations

import html
import shutil
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parent
DATA_DIR = PROJECT_ROOT / "data"
DB_PATH = DATA_DIR / "cosmetics.db"
DIST_DIR = PROJECT_ROOT / "dist"
DIST_IMAGES_DIR = DIST_DIR / "images"

SITE_TITLE = "Cosmetics"
EMPTY_MESSAGE = "No hay productos cargados"
PLACEHOLDER_TEXT = "Sin foto"


@dataclass(frozen=True)
class BuildResult:
    output_file: Path
    rows: int
    copied_images: int


def connect_read_only(db_path: Path | str = DB_PATH) -> sqlite3.Connection:
    path = Path(db_path)
    if not path.exists():
        raise FileNotFoundError(f"No existe la base de datos esperada: {path}")

    uri = f"file:{path.resolve().as_posix()}?mode=ro"
    return sqlite3.connect(uri, uri=True)


def get_inventory(db_path: Path | str = DB_PATH) -> list[dict[str, Any]]:
    query = """
        SELECT
            purchases.id AS purchase_id,
            products.brand,
            products.name,
            products.size,
            purchases.price_bob,
            purchases.purchase_date,
            purchases.finish_date,
            purchases.image_path
        FROM purchases
        JOIN products ON products.id = purchases.product_id
        ORDER BY purchases.purchase_date DESC, purchases.id DESC
    """

    with connect_read_only(db_path) as connection:
        connection.row_factory = sqlite3.Row
        rows = connection.execute(query).fetchall()

    return [dict(row) for row in rows]


def format_price(price_bob: int) -> str:
    return f"Bs {int(price_bob) / 100:.2f}"


def resolve_image(image_path: str | None, data_dir: Path | str = DATA_DIR) -> Path | None:
    if not image_path:
        return None

    root = Path(data_dir).resolve()
    candidate = (root / image_path).resolve()
    try:
        candidate.relative_to(root)
    except ValueError:
        return None

    return candidate if candidate.is_file() else None


def build_site(
    db_path: Path | str = DB_PATH,
    data_dir: Path | str = DATA_DIR,
    dist_dir: Path | str = DIST_DIR,
) -> BuildResult:
    rows = get_inventory(db_path)
    output_dir = Path(dist_dir)
    image_dir = output_dir / "images"

    if output_dir.exists():
        shutil.rmtree(output_dir)
    image_dir.mkdir(parents=True, exist_ok=True)

    prepared_rows, copied_images = prepare_rows(rows, data_dir, image_dir)
    output_file = output_dir / "index.html"
    output_file.write_text(render_document(prepared_rows), encoding="utf-8")
    (output_dir / ".nojekyll").write_text("", encoding="utf-8")

    return BuildResult(output_file=output_file, rows=len(rows), copied_images=copied_images)


def prepare_rows(
    rows: list[dict[str, Any]],
    data_dir: Path | str = DATA_DIR,
    output_images_dir: Path | str = DIST_IMAGES_DIR,
) -> tuple[list[dict[str, Any]], int]:
    prepared: list[dict[str, Any]] = []
    copied = 0
    used_names: set[str] = set()
    output_dir = Path(output_images_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    for row in rows:
        image_src = resolve_image(row.get("image_path"), data_dir)
        image_url = None

        if image_src is not None:
            image_name = unique_image_name(row, image_src, used_names)
            shutil.copy2(image_src, output_dir / image_name)
            image_url = f"images/{image_name}"
            copied += 1

        prepared.append(
            {
                "purchase_id": row.get("purchase_id"),
                "brand": row.get("brand") or "",
                "name": row.get("name") or "",
                "size": row.get("size") or "",
                "price": format_price(int(row.get("price_bob") or 0)),
                "purchase_date": row.get("purchase_date") or "",
                "finish_date": row.get("finish_date") or "",
                "available": row.get("finish_date") is None,
                "image_url": image_url,
            }
        )

    return prepared, copied


def unique_image_name(row: dict[str, Any], image_path: Path, used_names: set[str]) -> str:
    raw_id = row.get("purchase_id") or len(used_names) + 1
    stem = f"purchase-{raw_id}"
    suffix = image_path.suffix.lower() or ".img"
    candidate = f"{stem}{suffix}"
    counter = 2

    while candidate in used_names:
        candidate = f"{stem}-{counter}{suffix}"
        counter += 1

    used_names.add(candidate)
    return candidate


def render_document(rows: list[dict[str, Any]]) -> str:
    cards = "\n".join(render_card(row) for row in rows)
    total = len(rows)
    available = sum(1 for row in rows if row["available"])

    return f"""<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(SITE_TITLE)}</title>
  <style>{CSS}</style>
</head>
<body>
  <main class="shell">
    <header class="hero">
      <div>
        <p class="eyebrow">Inventario personal</p>
        <h1>{html.escape(SITE_TITLE)}</h1>
        <p class="summary"><strong>{available}</strong> disponibles · <strong>{total}</strong> compras registradas</p>
      </div>
      <label class="switch">
        <input id="availableOnly" type="checkbox" checked>
        <span>Solo disponibles</span>
      </label>
    </header>

    <section class="toolbar" aria-label="Filtros">
      <input id="search" type="search" placeholder="Buscar por marca o producto" autocomplete="off">
    </section>

    <p id="empty" class="empty" hidden>{html.escape(EMPTY_MESSAGE)}</p>
    <section id="grid" class="grid" aria-live="polite">
      {cards}
    </section>
  </main>
  <script>{JS}</script>
</body>
</html>
"""


def render_card(row: dict[str, Any]) -> str:
    search_text = " ".join(
        str(row.get(key, "")) for key in ("brand", "name", "size", "purchase_date", "finish_date")
    ).lower()
    available = "true" if row["available"] else "false"
    image = render_image(row.get("image_url"), row.get("name") or "producto")
    status = "Disponible" if row["available"] else "Terminado"
    status_class = "available" if row["available"] else "finished"
    finished = row.get("finish_date") or "—"

    return f"""<article class="card" data-available="{available}" data-search="{html.escape(search_text, quote=True)}">
  {image}
  <div class="content">
    <div class="topline">
      <span class="brand">{html.escape(str(row.get("brand") or ""))}</span>
      <span class="badge {status_class}">{status}</span>
    </div>
    <h2>{html.escape(str(row.get("name") or ""))}</h2>
    <dl>
      <div><dt>Tamaño</dt><dd>{html.escape(str(row.get("size") or "—"))}</dd></div>
      <div><dt>Precio</dt><dd>{html.escape(str(row.get("price") or ""))}</dd></div>
      <div><dt>Compra</dt><dd>{html.escape(str(row.get("purchase_date") or "—"))}</dd></div>
      <div><dt>Fin</dt><dd>{html.escape(str(finished))}</dd></div>
    </dl>
  </div>
</article>"""


def render_image(image_url: str | None, name: str) -> str:
    if not image_url:
        return f'<div class="photo placeholder">{html.escape(PLACEHOLDER_TEXT)}</div>'

    safe_url = html.escape(image_url, quote=True)
    safe_alt = html.escape(f"Foto de {name}", quote=True)
    return f'<a class="photo" href="{safe_url}" target="_blank" rel="noopener"><img src="{safe_url}" alt="{safe_alt}" loading="lazy"></a>'


CSS = """
:root {
  color-scheme: light;
  --bg: #f7f2ea;
  --panel: #fffaf2;
  --ink: #241f1a;
  --muted: #74695d;
  --line: #e4d8ca;
  --accent: #8b4a2f;
  --ok: #276749;
  --done: #8a4b15;
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

* { box-sizing: border-box; }
body { margin: 0; background: var(--bg); color: var(--ink); }
.shell { margin: 0 auto; max-width: 1180px; padding: 32px 20px 48px; }
.hero { align-items: end; display: flex; gap: 24px; justify-content: space-between; margin-bottom: 24px; }
.eyebrow { color: var(--accent); font-size: .78rem; font-weight: 800; letter-spacing: .12em; margin: 0 0 6px; text-transform: uppercase; }
h1 { font-size: clamp(2.2rem, 5vw, 4.6rem); letter-spacing: -.07em; line-height: .9; margin: 0; }
.summary { color: var(--muted); margin: 12px 0 0; }
.switch { align-items: center; background: var(--panel); border: 1px solid var(--line); border-radius: 999px; cursor: pointer; display: flex; font-weight: 700; gap: 10px; padding: 12px 16px; white-space: nowrap; }
.switch input { accent-color: var(--accent); height: 18px; width: 18px; }
.toolbar { margin: 0 0 22px; }
.toolbar input { background: var(--panel); border: 1px solid var(--line); border-radius: 18px; color: var(--ink); font: inherit; outline: none; padding: 16px 18px; width: 100%; }
.toolbar input:focus { border-color: var(--accent); box-shadow: 0 0 0 4px rgb(139 74 47 / 14%); }
.grid { display: grid; gap: 18px; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); }
.card { background: var(--panel); border: 1px solid var(--line); border-radius: 26px; box-shadow: 0 18px 48px rgb(56 40 24 / 8%); overflow: hidden; }
.photo { align-items: center; aspect-ratio: 4 / 3; background: #eadfd2; color: var(--muted); display: flex; justify-content: center; text-decoration: none; width: 100%; }
.photo img { height: 100%; object-fit: cover; width: 100%; }
.placeholder { border-bottom: 1px dashed var(--line); font-weight: 800; }
.content { padding: 18px; }
.topline { align-items: center; display: flex; gap: 10px; justify-content: space-between; }
.brand { color: var(--muted); font-size: .82rem; font-weight: 800; letter-spacing: .06em; text-transform: uppercase; }
.badge { border-radius: 999px; font-size: .72rem; font-weight: 900; padding: 6px 9px; }
.badge.available { background: rgb(39 103 73 / 12%); color: var(--ok); }
.badge.finished { background: rgb(138 75 21 / 12%); color: var(--done); }
h2 { font-size: 1.18rem; letter-spacing: -.02em; line-height: 1.15; margin: 14px 0 18px; }
dl { display: grid; gap: 12px; grid-template-columns: 1fr 1fr; margin: 0; }
dt { color: var(--muted); font-size: .72rem; font-weight: 800; text-transform: uppercase; }
dd { font-weight: 750; margin: 2px 0 0; }
.empty { background: var(--panel); border: 1px solid var(--line); border-radius: 18px; color: var(--muted); font-weight: 800; padding: 18px; text-align: center; }
[hidden] { display: none !important; }

@media (max-width: 680px) {
  .hero { align-items: stretch; flex-direction: column; }
  .switch { justify-content: center; }
}
"""


JS = """
const search = document.querySelector('#search');
const availableOnly = document.querySelector('#availableOnly');
const cards = [...document.querySelectorAll('.card')];
const empty = document.querySelector('#empty');

function normalize(value) {
  return value.trim().toLocaleLowerCase('es');
}

function applyFilters() {
  const term = normalize(search.value);
  const onlyAvailable = availableOnly.checked;
  let visible = 0;

  for (const card of cards) {
    const matchesAvailability = !onlyAvailable || card.dataset.available === 'true';
    const matchesSearch = !term || card.dataset.search.includes(term);
    const show = matchesAvailability && matchesSearch;
    card.hidden = !show;
    if (show) visible += 1;
  }

  empty.hidden = visible !== 0;
}

search.addEventListener('input', applyFilters);
availableOnly.addEventListener('change', applyFilters);
applyFilters();
"""


def main() -> None:
    result = build_site()
    print(f"Generado {result.output_file} con {result.rows} productos y {result.copied_images} imágenes.")


if __name__ == "__main__":
    main()
