from __future__ import annotations

import base64
import html
import mimetypes
import sqlite3
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
DB_PATH = DATA_DIR / "cosmetics.db"
PLACEHOLDER_TEXT = "Sin foto"
EMPTY_MESSAGE = "No hay productos cargados"


def connect_read_only(db_path: Path | str = DB_PATH) -> sqlite3.Connection:
    path = Path(db_path)
    if not path.exists():
        raise FileNotFoundError(f"No existe la base de datos esperada: {path}")
    uri = f"file:{path.resolve().as_posix()}?mode=ro"
    return sqlite3.connect(uri, uri=True)


def get_inventory(db_path: Path | str = DB_PATH, only_available: bool = False) -> list[dict[str, Any]]:
    where = "WHERE purchases.finish_date IS NULL" if only_available else ""
    query = f"""
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
        {where}
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


def render_inventory_table(rows: list[dict[str, Any]], data_dir: Path | str = DATA_DIR) -> str:
    body = "".join(_render_row(row, data_dir) for row in rows)
    return f"""
<style>
.inventory-table {{
    border-collapse: collapse;
    width: 100%;
    font-size: 0.92rem;
}}
.inventory-table th,
.inventory-table td {{
    border-bottom: 1px solid rgba(49, 51, 63, 0.16);
    padding: 0.55rem 0.65rem;
    text-align: left;
    vertical-align: middle;
}}
.inventory-table th {{
    color: rgba(49, 51, 63, 0.7);
    font-weight: 600;
}}
.inventory-table .thumb {{
    border-radius: 8px;
    display: block;
    height: 74px;
    object-fit: cover;
    width: 74px;
}}
.inventory-table .placeholder {{
    align-items: center;
    background: #f1f1ef;
    border: 1px dashed #c9c7c1;
    border-radius: 8px;
    color: #787774;
    display: flex;
    font-size: 0.78rem;
    height: 74px;
    justify-content: center;
    width: 74px;
}}
@media (max-width: 720px) {{
    .inventory-wrap {{ overflow-x: auto; }}
    .inventory-table {{ min-width: 760px; }}
}}
</style>
<div class="inventory-wrap">
<table class="inventory-table">
  <thead>
    <tr>
      <th>Foto</th>
      <th>Marca</th>
      <th>Nombre</th>
      <th>Tamaño</th>
      <th>Precio</th>
      <th>Fecha de compra</th>
      <th>Fecha de fin</th>
    </tr>
  </thead>
  <tbody>{body}</tbody>
</table>
</div>
"""


def _render_row(row: dict[str, Any], data_dir: Path | str) -> str:
    return """
    <tr>
      <td>{image}</td>
      <td>{brand}</td>
      <td>{name}</td>
      <td>{size}</td>
      <td>{price}</td>
      <td>{purchase_date}</td>
      <td>{finish_date}</td>
    </tr>
    """.format(
        image=_render_image(row.get("image_path"), data_dir),
        brand=html.escape(str(row.get("brand") or "")),
        name=html.escape(str(row.get("name") or "")),
        size=html.escape(str(row.get("size") or "")),
        price=html.escape(format_price(int(row["price_bob"]))),
        purchase_date=html.escape(str(row.get("purchase_date") or "")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def _render_image(image_path: str | None, data_dir: Path | str) -> str:
    path = resolve_image(image_path, data_dir)
    if path is None:
        return f'<div class="placeholder">{PLACEHOLDER_TEXT}</div>'

    mime_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    data_uri = f"data:{mime_type};base64,{encoded}"
    return (
        f'<a href="{data_uri}" target="_blank" rel="noopener" title="Abrir foto">'
        f'<img class="thumb" src="{data_uri}" alt="Foto de producto"></a>'
    )


def main() -> None:
    import streamlit as st

    st.set_page_config(page_title="Cosmetics", layout="wide")
    st.title("Inventario de cosméticos")

    only_available = st.toggle("Solo disponibles", value=True)
    try:
        rows = get_inventory(DB_PATH, only_available=only_available)
    except FileNotFoundError:
        st.error(f"No existe la base de datos esperada: {DB_PATH}")
        return
    except sqlite3.Error as exc:
        st.error(f"No se pudo leer la base de datos: {exc}")
        return

    if not rows:
        st.info(EMPTY_MESSAGE)
        return

    st.markdown(render_inventory_table(rows, DATA_DIR), unsafe_allow_html=True)


if __name__ == "__main__":
    main()
