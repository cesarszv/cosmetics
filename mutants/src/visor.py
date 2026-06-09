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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_connect_read_only__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_connect_read_only__mutmut)
def connect_read_only(db_path: Path | str = DB_PATH) -> sqlite3.Connection:
    path = Path(db_path)
    if not path.exists():
        raise FileNotFoundError(f"No existe la base de datos esperada: {path}")
    uri = f"file:{path.resolve().as_posix()}?mode=ro"
    return sqlite3.connect(uri, uri=True)


def x_connect_read_only__mutmut_orig(db_path: Path | str = DB_PATH) -> sqlite3.Connection:
    path = Path(db_path)
    if not path.exists():
        raise FileNotFoundError(f"No existe la base de datos esperada: {path}")
    uri = f"file:{path.resolve().as_posix()}?mode=ro"
    return sqlite3.connect(uri, uri=True)


def x_connect_read_only__mutmut_1(db_path: Path | str = DB_PATH) -> sqlite3.Connection:
    path = None
    if not path.exists():
        raise FileNotFoundError(f"No existe la base de datos esperada: {path}")
    uri = f"file:{path.resolve().as_posix()}?mode=ro"
    return sqlite3.connect(uri, uri=True)


def x_connect_read_only__mutmut_2(db_path: Path | str = DB_PATH) -> sqlite3.Connection:
    path = Path(None)
    if not path.exists():
        raise FileNotFoundError(f"No existe la base de datos esperada: {path}")
    uri = f"file:{path.resolve().as_posix()}?mode=ro"
    return sqlite3.connect(uri, uri=True)


def x_connect_read_only__mutmut_3(db_path: Path | str = DB_PATH) -> sqlite3.Connection:
    path = Path(db_path)
    if path.exists():
        raise FileNotFoundError(f"No existe la base de datos esperada: {path}")
    uri = f"file:{path.resolve().as_posix()}?mode=ro"
    return sqlite3.connect(uri, uri=True)


def x_connect_read_only__mutmut_4(db_path: Path | str = DB_PATH) -> sqlite3.Connection:
    path = Path(db_path)
    if not path.exists():
        raise FileNotFoundError(None)
    uri = f"file:{path.resolve().as_posix()}?mode=ro"
    return sqlite3.connect(uri, uri=True)


def x_connect_read_only__mutmut_5(db_path: Path | str = DB_PATH) -> sqlite3.Connection:
    path = Path(db_path)
    if not path.exists():
        raise FileNotFoundError(f"No existe la base de datos esperada: {path}")
    uri = None
    return sqlite3.connect(uri, uri=True)


def x_connect_read_only__mutmut_6(db_path: Path | str = DB_PATH) -> sqlite3.Connection:
    path = Path(db_path)
    if not path.exists():
        raise FileNotFoundError(f"No existe la base de datos esperada: {path}")
    uri = f"file:{path.resolve().as_posix()}?mode=ro"
    return sqlite3.connect(None, uri=True)


def x_connect_read_only__mutmut_7(db_path: Path | str = DB_PATH) -> sqlite3.Connection:
    path = Path(db_path)
    if not path.exists():
        raise FileNotFoundError(f"No existe la base de datos esperada: {path}")
    uri = f"file:{path.resolve().as_posix()}?mode=ro"
    return sqlite3.connect(uri, uri=None)


def x_connect_read_only__mutmut_8(db_path: Path | str = DB_PATH) -> sqlite3.Connection:
    path = Path(db_path)
    if not path.exists():
        raise FileNotFoundError(f"No existe la base de datos esperada: {path}")
    uri = f"file:{path.resolve().as_posix()}?mode=ro"
    return sqlite3.connect(uri=True)


def x_connect_read_only__mutmut_9(db_path: Path | str = DB_PATH) -> sqlite3.Connection:
    path = Path(db_path)
    if not path.exists():
        raise FileNotFoundError(f"No existe la base de datos esperada: {path}")
    uri = f"file:{path.resolve().as_posix()}?mode=ro"
    return sqlite3.connect(uri, )


def x_connect_read_only__mutmut_10(db_path: Path | str = DB_PATH) -> sqlite3.Connection:
    path = Path(db_path)
    if not path.exists():
        raise FileNotFoundError(f"No existe la base de datos esperada: {path}")
    uri = f"file:{path.resolve().as_posix()}?mode=ro"
    return sqlite3.connect(uri, uri=False)

mutants_x_connect_read_only__mutmut['_mutmut_orig'] = x_connect_read_only__mutmut_orig # type: ignore # mutmut generated
mutants_x_connect_read_only__mutmut['x_connect_read_only__mutmut_1'] = x_connect_read_only__mutmut_1 # type: ignore # mutmut generated
mutants_x_connect_read_only__mutmut['x_connect_read_only__mutmut_2'] = x_connect_read_only__mutmut_2 # type: ignore # mutmut generated
mutants_x_connect_read_only__mutmut['x_connect_read_only__mutmut_3'] = x_connect_read_only__mutmut_3 # type: ignore # mutmut generated
mutants_x_connect_read_only__mutmut['x_connect_read_only__mutmut_4'] = x_connect_read_only__mutmut_4 # type: ignore # mutmut generated
mutants_x_connect_read_only__mutmut['x_connect_read_only__mutmut_5'] = x_connect_read_only__mutmut_5 # type: ignore # mutmut generated
mutants_x_connect_read_only__mutmut['x_connect_read_only__mutmut_6'] = x_connect_read_only__mutmut_6 # type: ignore # mutmut generated
mutants_x_connect_read_only__mutmut['x_connect_read_only__mutmut_7'] = x_connect_read_only__mutmut_7 # type: ignore # mutmut generated
mutants_x_connect_read_only__mutmut['x_connect_read_only__mutmut_8'] = x_connect_read_only__mutmut_8 # type: ignore # mutmut generated
mutants_x_connect_read_only__mutmut['x_connect_read_only__mutmut_9'] = x_connect_read_only__mutmut_9 # type: ignore # mutmut generated
mutants_x_connect_read_only__mutmut['x_connect_read_only__mutmut_10'] = x_connect_read_only__mutmut_10 # type: ignore # mutmut generated
mutants_x_get_inventory__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_inventory__mutmut)
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


def x_get_inventory__mutmut_orig(db_path: Path | str = DB_PATH, only_available: bool = False) -> list[dict[str, Any]]:
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


def x_get_inventory__mutmut_1(db_path: Path | str = DB_PATH, only_available: bool = True) -> list[dict[str, Any]]:
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


def x_get_inventory__mutmut_2(db_path: Path | str = DB_PATH, only_available: bool = False) -> list[dict[str, Any]]:
    where = None
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


def x_get_inventory__mutmut_3(db_path: Path | str = DB_PATH, only_available: bool = False) -> list[dict[str, Any]]:
    where = "XXWHERE purchases.finish_date IS NULLXX" if only_available else ""
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


def x_get_inventory__mutmut_4(db_path: Path | str = DB_PATH, only_available: bool = False) -> list[dict[str, Any]]:
    where = "where purchases.finish_date is null" if only_available else ""
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


def x_get_inventory__mutmut_5(db_path: Path | str = DB_PATH, only_available: bool = False) -> list[dict[str, Any]]:
    where = "WHERE PURCHASES.FINISH_DATE IS NULL" if only_available else ""
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


def x_get_inventory__mutmut_6(db_path: Path | str = DB_PATH, only_available: bool = False) -> list[dict[str, Any]]:
    where = "WHERE purchases.finish_date IS NULL" if only_available else "XXXX"
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


def x_get_inventory__mutmut_7(db_path: Path | str = DB_PATH, only_available: bool = False) -> list[dict[str, Any]]:
    where = "WHERE purchases.finish_date IS NULL" if only_available else ""
    query = None
    with connect_read_only(db_path) as connection:
        connection.row_factory = sqlite3.Row
        rows = connection.execute(query).fetchall()
    return [dict(row) for row in rows]


def x_get_inventory__mutmut_8(db_path: Path | str = DB_PATH, only_available: bool = False) -> list[dict[str, Any]]:
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
    with connect_read_only(None) as connection:
        connection.row_factory = sqlite3.Row
        rows = connection.execute(query).fetchall()
    return [dict(row) for row in rows]


def x_get_inventory__mutmut_9(db_path: Path | str = DB_PATH, only_available: bool = False) -> list[dict[str, Any]]:
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
        connection.row_factory = None
        rows = connection.execute(query).fetchall()
    return [dict(row) for row in rows]


def x_get_inventory__mutmut_10(db_path: Path | str = DB_PATH, only_available: bool = False) -> list[dict[str, Any]]:
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
        rows = None
    return [dict(row) for row in rows]


def x_get_inventory__mutmut_11(db_path: Path | str = DB_PATH, only_available: bool = False) -> list[dict[str, Any]]:
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
        rows = connection.execute(None).fetchall()
    return [dict(row) for row in rows]


def x_get_inventory__mutmut_12(db_path: Path | str = DB_PATH, only_available: bool = False) -> list[dict[str, Any]]:
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
    return [dict(None) for row in rows]

mutants_x_get_inventory__mutmut['_mutmut_orig'] = x_get_inventory__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_inventory__mutmut['x_get_inventory__mutmut_1'] = x_get_inventory__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_inventory__mutmut['x_get_inventory__mutmut_2'] = x_get_inventory__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_inventory__mutmut['x_get_inventory__mutmut_3'] = x_get_inventory__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_inventory__mutmut['x_get_inventory__mutmut_4'] = x_get_inventory__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_inventory__mutmut['x_get_inventory__mutmut_5'] = x_get_inventory__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_inventory__mutmut['x_get_inventory__mutmut_6'] = x_get_inventory__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_inventory__mutmut['x_get_inventory__mutmut_7'] = x_get_inventory__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_inventory__mutmut['x_get_inventory__mutmut_8'] = x_get_inventory__mutmut_8 # type: ignore # mutmut generated
mutants_x_get_inventory__mutmut['x_get_inventory__mutmut_9'] = x_get_inventory__mutmut_9 # type: ignore # mutmut generated
mutants_x_get_inventory__mutmut['x_get_inventory__mutmut_10'] = x_get_inventory__mutmut_10 # type: ignore # mutmut generated
mutants_x_get_inventory__mutmut['x_get_inventory__mutmut_11'] = x_get_inventory__mutmut_11 # type: ignore # mutmut generated
mutants_x_get_inventory__mutmut['x_get_inventory__mutmut_12'] = x_get_inventory__mutmut_12 # type: ignore # mutmut generated
mutants_x_format_price__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_format_price__mutmut)
def format_price(price_bob: int) -> str:
    return f"Bs {int(price_bob) / 100:.2f}"


def x_format_price__mutmut_orig(price_bob: int) -> str:
    return f"Bs {int(price_bob) / 100:.2f}"


def x_format_price__mutmut_1(price_bob: int) -> str:
    return f"Bs {int(price_bob) * 100:.2f}"


def x_format_price__mutmut_2(price_bob: int) -> str:
    return f"Bs {int(None) / 100:.2f}"


def x_format_price__mutmut_3(price_bob: int) -> str:
    return f"Bs {int(price_bob) / 101:.2f}"

mutants_x_format_price__mutmut['_mutmut_orig'] = x_format_price__mutmut_orig # type: ignore # mutmut generated
mutants_x_format_price__mutmut['x_format_price__mutmut_1'] = x_format_price__mutmut_1 # type: ignore # mutmut generated
mutants_x_format_price__mutmut['x_format_price__mutmut_2'] = x_format_price__mutmut_2 # type: ignore # mutmut generated
mutants_x_format_price__mutmut['x_format_price__mutmut_3'] = x_format_price__mutmut_3 # type: ignore # mutmut generated
mutants_x_resolve_image__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_resolve_image__mutmut)
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


def x_resolve_image__mutmut_orig(image_path: str | None, data_dir: Path | str = DATA_DIR) -> Path | None:
    if not image_path:
        return None

    root = Path(data_dir).resolve()
    candidate = (root / image_path).resolve()
    try:
        candidate.relative_to(root)
    except ValueError:
        return None
    return candidate if candidate.is_file() else None


def x_resolve_image__mutmut_1(image_path: str | None, data_dir: Path | str = DATA_DIR) -> Path | None:
    if image_path:
        return None

    root = Path(data_dir).resolve()
    candidate = (root / image_path).resolve()
    try:
        candidate.relative_to(root)
    except ValueError:
        return None
    return candidate if candidate.is_file() else None


def x_resolve_image__mutmut_2(image_path: str | None, data_dir: Path | str = DATA_DIR) -> Path | None:
    if not image_path:
        return None

    root = None
    candidate = (root / image_path).resolve()
    try:
        candidate.relative_to(root)
    except ValueError:
        return None
    return candidate if candidate.is_file() else None


def x_resolve_image__mutmut_3(image_path: str | None, data_dir: Path | str = DATA_DIR) -> Path | None:
    if not image_path:
        return None

    root = Path(None).resolve()
    candidate = (root / image_path).resolve()
    try:
        candidate.relative_to(root)
    except ValueError:
        return None
    return candidate if candidate.is_file() else None


def x_resolve_image__mutmut_4(image_path: str | None, data_dir: Path | str = DATA_DIR) -> Path | None:
    if not image_path:
        return None

    root = Path(data_dir).resolve()
    candidate = None
    try:
        candidate.relative_to(root)
    except ValueError:
        return None
    return candidate if candidate.is_file() else None


def x_resolve_image__mutmut_5(image_path: str | None, data_dir: Path | str = DATA_DIR) -> Path | None:
    if not image_path:
        return None

    root = Path(data_dir).resolve()
    candidate = (root * image_path).resolve()
    try:
        candidate.relative_to(root)
    except ValueError:
        return None
    return candidate if candidate.is_file() else None


def x_resolve_image__mutmut_6(image_path: str | None, data_dir: Path | str = DATA_DIR) -> Path | None:
    if not image_path:
        return None

    root = Path(data_dir).resolve()
    candidate = (root / image_path).resolve()
    try:
        candidate.relative_to(None)
    except ValueError:
        return None
    return candidate if candidate.is_file() else None

mutants_x_resolve_image__mutmut['_mutmut_orig'] = x_resolve_image__mutmut_orig # type: ignore # mutmut generated
mutants_x_resolve_image__mutmut['x_resolve_image__mutmut_1'] = x_resolve_image__mutmut_1 # type: ignore # mutmut generated
mutants_x_resolve_image__mutmut['x_resolve_image__mutmut_2'] = x_resolve_image__mutmut_2 # type: ignore # mutmut generated
mutants_x_resolve_image__mutmut['x_resolve_image__mutmut_3'] = x_resolve_image__mutmut_3 # type: ignore # mutmut generated
mutants_x_resolve_image__mutmut['x_resolve_image__mutmut_4'] = x_resolve_image__mutmut_4 # type: ignore # mutmut generated
mutants_x_resolve_image__mutmut['x_resolve_image__mutmut_5'] = x_resolve_image__mutmut_5 # type: ignore # mutmut generated
mutants_x_resolve_image__mutmut['x_resolve_image__mutmut_6'] = x_resolve_image__mutmut_6 # type: ignore # mutmut generated
mutants_x_render_inventory_table__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_render_inventory_table__mutmut)
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


def x_render_inventory_table__mutmut_orig(rows: list[dict[str, Any]], data_dir: Path | str = DATA_DIR) -> str:
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


def x_render_inventory_table__mutmut_1(rows: list[dict[str, Any]], data_dir: Path | str = DATA_DIR) -> str:
    body = None
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


def x_render_inventory_table__mutmut_2(rows: list[dict[str, Any]], data_dir: Path | str = DATA_DIR) -> str:
    body = "".join(None)
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


def x_render_inventory_table__mutmut_3(rows: list[dict[str, Any]], data_dir: Path | str = DATA_DIR) -> str:
    body = "XXXX".join(_render_row(row, data_dir) for row in rows)
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


def x_render_inventory_table__mutmut_4(rows: list[dict[str, Any]], data_dir: Path | str = DATA_DIR) -> str:
    body = "".join(_render_row(None, data_dir) for row in rows)
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


def x_render_inventory_table__mutmut_5(rows: list[dict[str, Any]], data_dir: Path | str = DATA_DIR) -> str:
    body = "".join(_render_row(row, None) for row in rows)
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


def x_render_inventory_table__mutmut_6(rows: list[dict[str, Any]], data_dir: Path | str = DATA_DIR) -> str:
    body = "".join(_render_row(data_dir) for row in rows)
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


def x_render_inventory_table__mutmut_7(rows: list[dict[str, Any]], data_dir: Path | str = DATA_DIR) -> str:
    body = "".join(_render_row(row, ) for row in rows)
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

mutants_x_render_inventory_table__mutmut['_mutmut_orig'] = x_render_inventory_table__mutmut_orig # type: ignore # mutmut generated
mutants_x_render_inventory_table__mutmut['x_render_inventory_table__mutmut_1'] = x_render_inventory_table__mutmut_1 # type: ignore # mutmut generated
mutants_x_render_inventory_table__mutmut['x_render_inventory_table__mutmut_2'] = x_render_inventory_table__mutmut_2 # type: ignore # mutmut generated
mutants_x_render_inventory_table__mutmut['x_render_inventory_table__mutmut_3'] = x_render_inventory_table__mutmut_3 # type: ignore # mutmut generated
mutants_x_render_inventory_table__mutmut['x_render_inventory_table__mutmut_4'] = x_render_inventory_table__mutmut_4 # type: ignore # mutmut generated
mutants_x_render_inventory_table__mutmut['x_render_inventory_table__mutmut_5'] = x_render_inventory_table__mutmut_5 # type: ignore # mutmut generated
mutants_x_render_inventory_table__mutmut['x_render_inventory_table__mutmut_6'] = x_render_inventory_table__mutmut_6 # type: ignore # mutmut generated
mutants_x_render_inventory_table__mutmut['x_render_inventory_table__mutmut_7'] = x_render_inventory_table__mutmut_7 # type: ignore # mutmut generated
mutants_x__render_row__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__render_row__mutmut)
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


def x__render_row__mutmut_orig(row: dict[str, Any], data_dir: Path | str) -> str:
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


def x__render_row__mutmut_1(row: dict[str, Any], data_dir: Path | str) -> str:
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
        image=None,
        brand=html.escape(str(row.get("brand") or "")),
        name=html.escape(str(row.get("name") or "")),
        size=html.escape(str(row.get("size") or "")),
        price=html.escape(format_price(int(row["price_bob"]))),
        purchase_date=html.escape(str(row.get("purchase_date") or "")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_2(row: dict[str, Any], data_dir: Path | str) -> str:
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
        brand=None,
        name=html.escape(str(row.get("name") or "")),
        size=html.escape(str(row.get("size") or "")),
        price=html.escape(format_price(int(row["price_bob"]))),
        purchase_date=html.escape(str(row.get("purchase_date") or "")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_3(row: dict[str, Any], data_dir: Path | str) -> str:
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
        name=None,
        size=html.escape(str(row.get("size") or "")),
        price=html.escape(format_price(int(row["price_bob"]))),
        purchase_date=html.escape(str(row.get("purchase_date") or "")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_4(row: dict[str, Any], data_dir: Path | str) -> str:
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
        size=None,
        price=html.escape(format_price(int(row["price_bob"]))),
        purchase_date=html.escape(str(row.get("purchase_date") or "")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_5(row: dict[str, Any], data_dir: Path | str) -> str:
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
        price=None,
        purchase_date=html.escape(str(row.get("purchase_date") or "")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_6(row: dict[str, Any], data_dir: Path | str) -> str:
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
        purchase_date=None,
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_7(row: dict[str, Any], data_dir: Path | str) -> str:
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
        finish_date=None,
    )


def x__render_row__mutmut_8(row: dict[str, Any], data_dir: Path | str) -> str:
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
        brand=html.escape(str(row.get("brand") or "")),
        name=html.escape(str(row.get("name") or "")),
        size=html.escape(str(row.get("size") or "")),
        price=html.escape(format_price(int(row["price_bob"]))),
        purchase_date=html.escape(str(row.get("purchase_date") or "")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_9(row: dict[str, Any], data_dir: Path | str) -> str:
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
        name=html.escape(str(row.get("name") or "")),
        size=html.escape(str(row.get("size") or "")),
        price=html.escape(format_price(int(row["price_bob"]))),
        purchase_date=html.escape(str(row.get("purchase_date") or "")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_10(row: dict[str, Any], data_dir: Path | str) -> str:
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
        size=html.escape(str(row.get("size") or "")),
        price=html.escape(format_price(int(row["price_bob"]))),
        purchase_date=html.escape(str(row.get("purchase_date") or "")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_11(row: dict[str, Any], data_dir: Path | str) -> str:
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
        price=html.escape(format_price(int(row["price_bob"]))),
        purchase_date=html.escape(str(row.get("purchase_date") or "")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_12(row: dict[str, Any], data_dir: Path | str) -> str:
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
        purchase_date=html.escape(str(row.get("purchase_date") or "")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_13(row: dict[str, Any], data_dir: Path | str) -> str:
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
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_14(row: dict[str, Any], data_dir: Path | str) -> str:
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
        )


def x__render_row__mutmut_15(row: dict[str, Any], data_dir: Path | str) -> str:
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
        image=_render_image(None, data_dir),
        brand=html.escape(str(row.get("brand") or "")),
        name=html.escape(str(row.get("name") or "")),
        size=html.escape(str(row.get("size") or "")),
        price=html.escape(format_price(int(row["price_bob"]))),
        purchase_date=html.escape(str(row.get("purchase_date") or "")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_16(row: dict[str, Any], data_dir: Path | str) -> str:
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
        image=_render_image(row.get("image_path"), None),
        brand=html.escape(str(row.get("brand") or "")),
        name=html.escape(str(row.get("name") or "")),
        size=html.escape(str(row.get("size") or "")),
        price=html.escape(format_price(int(row["price_bob"]))),
        purchase_date=html.escape(str(row.get("purchase_date") or "")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_17(row: dict[str, Any], data_dir: Path | str) -> str:
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
        image=_render_image(data_dir),
        brand=html.escape(str(row.get("brand") or "")),
        name=html.escape(str(row.get("name") or "")),
        size=html.escape(str(row.get("size") or "")),
        price=html.escape(format_price(int(row["price_bob"]))),
        purchase_date=html.escape(str(row.get("purchase_date") or "")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_18(row: dict[str, Any], data_dir: Path | str) -> str:
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
        image=_render_image(row.get("image_path"), ),
        brand=html.escape(str(row.get("brand") or "")),
        name=html.escape(str(row.get("name") or "")),
        size=html.escape(str(row.get("size") or "")),
        price=html.escape(format_price(int(row["price_bob"]))),
        purchase_date=html.escape(str(row.get("purchase_date") or "")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_19(row: dict[str, Any], data_dir: Path | str) -> str:
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
        image=_render_image(row.get(None), data_dir),
        brand=html.escape(str(row.get("brand") or "")),
        name=html.escape(str(row.get("name") or "")),
        size=html.escape(str(row.get("size") or "")),
        price=html.escape(format_price(int(row["price_bob"]))),
        purchase_date=html.escape(str(row.get("purchase_date") or "")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_20(row: dict[str, Any], data_dir: Path | str) -> str:
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
        image=_render_image(row.get("XXimage_pathXX"), data_dir),
        brand=html.escape(str(row.get("brand") or "")),
        name=html.escape(str(row.get("name") or "")),
        size=html.escape(str(row.get("size") or "")),
        price=html.escape(format_price(int(row["price_bob"]))),
        purchase_date=html.escape(str(row.get("purchase_date") or "")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_21(row: dict[str, Any], data_dir: Path | str) -> str:
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
        image=_render_image(row.get("IMAGE_PATH"), data_dir),
        brand=html.escape(str(row.get("brand") or "")),
        name=html.escape(str(row.get("name") or "")),
        size=html.escape(str(row.get("size") or "")),
        price=html.escape(format_price(int(row["price_bob"]))),
        purchase_date=html.escape(str(row.get("purchase_date") or "")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_22(row: dict[str, Any], data_dir: Path | str) -> str:
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
        brand=html.escape(None),
        name=html.escape(str(row.get("name") or "")),
        size=html.escape(str(row.get("size") or "")),
        price=html.escape(format_price(int(row["price_bob"]))),
        purchase_date=html.escape(str(row.get("purchase_date") or "")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_23(row: dict[str, Any], data_dir: Path | str) -> str:
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
        brand=html.escape(str(None)),
        name=html.escape(str(row.get("name") or "")),
        size=html.escape(str(row.get("size") or "")),
        price=html.escape(format_price(int(row["price_bob"]))),
        purchase_date=html.escape(str(row.get("purchase_date") or "")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_24(row: dict[str, Any], data_dir: Path | str) -> str:
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
        brand=html.escape(str(row.get("brand") and "")),
        name=html.escape(str(row.get("name") or "")),
        size=html.escape(str(row.get("size") or "")),
        price=html.escape(format_price(int(row["price_bob"]))),
        purchase_date=html.escape(str(row.get("purchase_date") or "")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_25(row: dict[str, Any], data_dir: Path | str) -> str:
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
        brand=html.escape(str(row.get(None) or "")),
        name=html.escape(str(row.get("name") or "")),
        size=html.escape(str(row.get("size") or "")),
        price=html.escape(format_price(int(row["price_bob"]))),
        purchase_date=html.escape(str(row.get("purchase_date") or "")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_26(row: dict[str, Any], data_dir: Path | str) -> str:
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
        brand=html.escape(str(row.get("XXbrandXX") or "")),
        name=html.escape(str(row.get("name") or "")),
        size=html.escape(str(row.get("size") or "")),
        price=html.escape(format_price(int(row["price_bob"]))),
        purchase_date=html.escape(str(row.get("purchase_date") or "")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_27(row: dict[str, Any], data_dir: Path | str) -> str:
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
        brand=html.escape(str(row.get("BRAND") or "")),
        name=html.escape(str(row.get("name") or "")),
        size=html.escape(str(row.get("size") or "")),
        price=html.escape(format_price(int(row["price_bob"]))),
        purchase_date=html.escape(str(row.get("purchase_date") or "")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_28(row: dict[str, Any], data_dir: Path | str) -> str:
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
        brand=html.escape(str(row.get("brand") or "XXXX")),
        name=html.escape(str(row.get("name") or "")),
        size=html.escape(str(row.get("size") or "")),
        price=html.escape(format_price(int(row["price_bob"]))),
        purchase_date=html.escape(str(row.get("purchase_date") or "")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_29(row: dict[str, Any], data_dir: Path | str) -> str:
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
        name=html.escape(None),
        size=html.escape(str(row.get("size") or "")),
        price=html.escape(format_price(int(row["price_bob"]))),
        purchase_date=html.escape(str(row.get("purchase_date") or "")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_30(row: dict[str, Any], data_dir: Path | str) -> str:
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
        name=html.escape(str(None)),
        size=html.escape(str(row.get("size") or "")),
        price=html.escape(format_price(int(row["price_bob"]))),
        purchase_date=html.escape(str(row.get("purchase_date") or "")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_31(row: dict[str, Any], data_dir: Path | str) -> str:
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
        name=html.escape(str(row.get("name") and "")),
        size=html.escape(str(row.get("size") or "")),
        price=html.escape(format_price(int(row["price_bob"]))),
        purchase_date=html.escape(str(row.get("purchase_date") or "")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_32(row: dict[str, Any], data_dir: Path | str) -> str:
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
        name=html.escape(str(row.get(None) or "")),
        size=html.escape(str(row.get("size") or "")),
        price=html.escape(format_price(int(row["price_bob"]))),
        purchase_date=html.escape(str(row.get("purchase_date") or "")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_33(row: dict[str, Any], data_dir: Path | str) -> str:
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
        name=html.escape(str(row.get("XXnameXX") or "")),
        size=html.escape(str(row.get("size") or "")),
        price=html.escape(format_price(int(row["price_bob"]))),
        purchase_date=html.escape(str(row.get("purchase_date") or "")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_34(row: dict[str, Any], data_dir: Path | str) -> str:
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
        name=html.escape(str(row.get("NAME") or "")),
        size=html.escape(str(row.get("size") or "")),
        price=html.escape(format_price(int(row["price_bob"]))),
        purchase_date=html.escape(str(row.get("purchase_date") or "")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_35(row: dict[str, Any], data_dir: Path | str) -> str:
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
        name=html.escape(str(row.get("name") or "XXXX")),
        size=html.escape(str(row.get("size") or "")),
        price=html.escape(format_price(int(row["price_bob"]))),
        purchase_date=html.escape(str(row.get("purchase_date") or "")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_36(row: dict[str, Any], data_dir: Path | str) -> str:
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
        size=html.escape(None),
        price=html.escape(format_price(int(row["price_bob"]))),
        purchase_date=html.escape(str(row.get("purchase_date") or "")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_37(row: dict[str, Any], data_dir: Path | str) -> str:
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
        size=html.escape(str(None)),
        price=html.escape(format_price(int(row["price_bob"]))),
        purchase_date=html.escape(str(row.get("purchase_date") or "")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_38(row: dict[str, Any], data_dir: Path | str) -> str:
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
        size=html.escape(str(row.get("size") and "")),
        price=html.escape(format_price(int(row["price_bob"]))),
        purchase_date=html.escape(str(row.get("purchase_date") or "")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_39(row: dict[str, Any], data_dir: Path | str) -> str:
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
        size=html.escape(str(row.get(None) or "")),
        price=html.escape(format_price(int(row["price_bob"]))),
        purchase_date=html.escape(str(row.get("purchase_date") or "")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_40(row: dict[str, Any], data_dir: Path | str) -> str:
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
        size=html.escape(str(row.get("XXsizeXX") or "")),
        price=html.escape(format_price(int(row["price_bob"]))),
        purchase_date=html.escape(str(row.get("purchase_date") or "")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_41(row: dict[str, Any], data_dir: Path | str) -> str:
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
        size=html.escape(str(row.get("SIZE") or "")),
        price=html.escape(format_price(int(row["price_bob"]))),
        purchase_date=html.escape(str(row.get("purchase_date") or "")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_42(row: dict[str, Any], data_dir: Path | str) -> str:
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
        size=html.escape(str(row.get("size") or "XXXX")),
        price=html.escape(format_price(int(row["price_bob"]))),
        purchase_date=html.escape(str(row.get("purchase_date") or "")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_43(row: dict[str, Any], data_dir: Path | str) -> str:
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
        price=html.escape(None),
        purchase_date=html.escape(str(row.get("purchase_date") or "")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_44(row: dict[str, Any], data_dir: Path | str) -> str:
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
        price=html.escape(format_price(None)),
        purchase_date=html.escape(str(row.get("purchase_date") or "")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_45(row: dict[str, Any], data_dir: Path | str) -> str:
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
        price=html.escape(format_price(int(None))),
        purchase_date=html.escape(str(row.get("purchase_date") or "")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_46(row: dict[str, Any], data_dir: Path | str) -> str:
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
        price=html.escape(format_price(int(row["XXprice_bobXX"]))),
        purchase_date=html.escape(str(row.get("purchase_date") or "")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_47(row: dict[str, Any], data_dir: Path | str) -> str:
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
        price=html.escape(format_price(int(row["PRICE_BOB"]))),
        purchase_date=html.escape(str(row.get("purchase_date") or "")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_48(row: dict[str, Any], data_dir: Path | str) -> str:
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
        purchase_date=html.escape(None),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_49(row: dict[str, Any], data_dir: Path | str) -> str:
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
        purchase_date=html.escape(str(None)),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_50(row: dict[str, Any], data_dir: Path | str) -> str:
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
        purchase_date=html.escape(str(row.get("purchase_date") and "")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_51(row: dict[str, Any], data_dir: Path | str) -> str:
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
        purchase_date=html.escape(str(row.get(None) or "")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_52(row: dict[str, Any], data_dir: Path | str) -> str:
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
        purchase_date=html.escape(str(row.get("XXpurchase_dateXX") or "")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_53(row: dict[str, Any], data_dir: Path | str) -> str:
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
        purchase_date=html.escape(str(row.get("PURCHASE_DATE") or "")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_54(row: dict[str, Any], data_dir: Path | str) -> str:
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
        purchase_date=html.escape(str(row.get("purchase_date") or "XXXX")),
        finish_date=html.escape(str(row.get("finish_date") or "")),
    )


def x__render_row__mutmut_55(row: dict[str, Any], data_dir: Path | str) -> str:
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
        finish_date=html.escape(None),
    )


def x__render_row__mutmut_56(row: dict[str, Any], data_dir: Path | str) -> str:
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
        finish_date=html.escape(str(None)),
    )


def x__render_row__mutmut_57(row: dict[str, Any], data_dir: Path | str) -> str:
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
        finish_date=html.escape(str(row.get("finish_date") and "")),
    )


def x__render_row__mutmut_58(row: dict[str, Any], data_dir: Path | str) -> str:
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
        finish_date=html.escape(str(row.get(None) or "")),
    )


def x__render_row__mutmut_59(row: dict[str, Any], data_dir: Path | str) -> str:
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
        finish_date=html.escape(str(row.get("XXfinish_dateXX") or "")),
    )


def x__render_row__mutmut_60(row: dict[str, Any], data_dir: Path | str) -> str:
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
        finish_date=html.escape(str(row.get("FINISH_DATE") or "")),
    )


def x__render_row__mutmut_61(row: dict[str, Any], data_dir: Path | str) -> str:
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
        finish_date=html.escape(str(row.get("finish_date") or "XXXX")),
    )

mutants_x__render_row__mutmut['_mutmut_orig'] = x__render_row__mutmut_orig # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_1'] = x__render_row__mutmut_1 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_2'] = x__render_row__mutmut_2 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_3'] = x__render_row__mutmut_3 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_4'] = x__render_row__mutmut_4 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_5'] = x__render_row__mutmut_5 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_6'] = x__render_row__mutmut_6 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_7'] = x__render_row__mutmut_7 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_8'] = x__render_row__mutmut_8 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_9'] = x__render_row__mutmut_9 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_10'] = x__render_row__mutmut_10 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_11'] = x__render_row__mutmut_11 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_12'] = x__render_row__mutmut_12 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_13'] = x__render_row__mutmut_13 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_14'] = x__render_row__mutmut_14 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_15'] = x__render_row__mutmut_15 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_16'] = x__render_row__mutmut_16 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_17'] = x__render_row__mutmut_17 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_18'] = x__render_row__mutmut_18 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_19'] = x__render_row__mutmut_19 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_20'] = x__render_row__mutmut_20 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_21'] = x__render_row__mutmut_21 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_22'] = x__render_row__mutmut_22 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_23'] = x__render_row__mutmut_23 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_24'] = x__render_row__mutmut_24 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_25'] = x__render_row__mutmut_25 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_26'] = x__render_row__mutmut_26 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_27'] = x__render_row__mutmut_27 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_28'] = x__render_row__mutmut_28 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_29'] = x__render_row__mutmut_29 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_30'] = x__render_row__mutmut_30 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_31'] = x__render_row__mutmut_31 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_32'] = x__render_row__mutmut_32 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_33'] = x__render_row__mutmut_33 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_34'] = x__render_row__mutmut_34 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_35'] = x__render_row__mutmut_35 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_36'] = x__render_row__mutmut_36 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_37'] = x__render_row__mutmut_37 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_38'] = x__render_row__mutmut_38 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_39'] = x__render_row__mutmut_39 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_40'] = x__render_row__mutmut_40 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_41'] = x__render_row__mutmut_41 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_42'] = x__render_row__mutmut_42 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_43'] = x__render_row__mutmut_43 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_44'] = x__render_row__mutmut_44 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_45'] = x__render_row__mutmut_45 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_46'] = x__render_row__mutmut_46 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_47'] = x__render_row__mutmut_47 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_48'] = x__render_row__mutmut_48 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_49'] = x__render_row__mutmut_49 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_50'] = x__render_row__mutmut_50 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_51'] = x__render_row__mutmut_51 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_52'] = x__render_row__mutmut_52 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_53'] = x__render_row__mutmut_53 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_54'] = x__render_row__mutmut_54 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_55'] = x__render_row__mutmut_55 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_56'] = x__render_row__mutmut_56 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_57'] = x__render_row__mutmut_57 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_58'] = x__render_row__mutmut_58 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_59'] = x__render_row__mutmut_59 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_60'] = x__render_row__mutmut_60 # type: ignore # mutmut generated
mutants_x__render_row__mutmut['x__render_row__mutmut_61'] = x__render_row__mutmut_61 # type: ignore # mutmut generated
mutants_x__render_image__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__render_image__mutmut)
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


def x__render_image__mutmut_orig(image_path: str | None, data_dir: Path | str) -> str:
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


def x__render_image__mutmut_1(image_path: str | None, data_dir: Path | str) -> str:
    path = None
    if path is None:
        return f'<div class="placeholder">{PLACEHOLDER_TEXT}</div>'

    mime_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    data_uri = f"data:{mime_type};base64,{encoded}"
    return (
        f'<a href="{data_uri}" target="_blank" rel="noopener" title="Abrir foto">'
        f'<img class="thumb" src="{data_uri}" alt="Foto de producto"></a>'
    )


def x__render_image__mutmut_2(image_path: str | None, data_dir: Path | str) -> str:
    path = resolve_image(None, data_dir)
    if path is None:
        return f'<div class="placeholder">{PLACEHOLDER_TEXT}</div>'

    mime_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    data_uri = f"data:{mime_type};base64,{encoded}"
    return (
        f'<a href="{data_uri}" target="_blank" rel="noopener" title="Abrir foto">'
        f'<img class="thumb" src="{data_uri}" alt="Foto de producto"></a>'
    )


def x__render_image__mutmut_3(image_path: str | None, data_dir: Path | str) -> str:
    path = resolve_image(image_path, None)
    if path is None:
        return f'<div class="placeholder">{PLACEHOLDER_TEXT}</div>'

    mime_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    data_uri = f"data:{mime_type};base64,{encoded}"
    return (
        f'<a href="{data_uri}" target="_blank" rel="noopener" title="Abrir foto">'
        f'<img class="thumb" src="{data_uri}" alt="Foto de producto"></a>'
    )


def x__render_image__mutmut_4(image_path: str | None, data_dir: Path | str) -> str:
    path = resolve_image(data_dir)
    if path is None:
        return f'<div class="placeholder">{PLACEHOLDER_TEXT}</div>'

    mime_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    data_uri = f"data:{mime_type};base64,{encoded}"
    return (
        f'<a href="{data_uri}" target="_blank" rel="noopener" title="Abrir foto">'
        f'<img class="thumb" src="{data_uri}" alt="Foto de producto"></a>'
    )


def x__render_image__mutmut_5(image_path: str | None, data_dir: Path | str) -> str:
    path = resolve_image(image_path, )
    if path is None:
        return f'<div class="placeholder">{PLACEHOLDER_TEXT}</div>'

    mime_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    data_uri = f"data:{mime_type};base64,{encoded}"
    return (
        f'<a href="{data_uri}" target="_blank" rel="noopener" title="Abrir foto">'
        f'<img class="thumb" src="{data_uri}" alt="Foto de producto"></a>'
    )


def x__render_image__mutmut_6(image_path: str | None, data_dir: Path | str) -> str:
    path = resolve_image(image_path, data_dir)
    if path is not None:
        return f'<div class="placeholder">{PLACEHOLDER_TEXT}</div>'

    mime_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    data_uri = f"data:{mime_type};base64,{encoded}"
    return (
        f'<a href="{data_uri}" target="_blank" rel="noopener" title="Abrir foto">'
        f'<img class="thumb" src="{data_uri}" alt="Foto de producto"></a>'
    )


def x__render_image__mutmut_7(image_path: str | None, data_dir: Path | str) -> str:
    path = resolve_image(image_path, data_dir)
    if path is None:
        return f'<div class="placeholder">{PLACEHOLDER_TEXT}</div>'

    mime_type = None
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    data_uri = f"data:{mime_type};base64,{encoded}"
    return (
        f'<a href="{data_uri}" target="_blank" rel="noopener" title="Abrir foto">'
        f'<img class="thumb" src="{data_uri}" alt="Foto de producto"></a>'
    )


def x__render_image__mutmut_8(image_path: str | None, data_dir: Path | str) -> str:
    path = resolve_image(image_path, data_dir)
    if path is None:
        return f'<div class="placeholder">{PLACEHOLDER_TEXT}</div>'

    mime_type = mimetypes.guess_type(path.name)[0] and "application/octet-stream"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    data_uri = f"data:{mime_type};base64,{encoded}"
    return (
        f'<a href="{data_uri}" target="_blank" rel="noopener" title="Abrir foto">'
        f'<img class="thumb" src="{data_uri}" alt="Foto de producto"></a>'
    )


def x__render_image__mutmut_9(image_path: str | None, data_dir: Path | str) -> str:
    path = resolve_image(image_path, data_dir)
    if path is None:
        return f'<div class="placeholder">{PLACEHOLDER_TEXT}</div>'

    mime_type = mimetypes.guess_type(None)[0] or "application/octet-stream"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    data_uri = f"data:{mime_type};base64,{encoded}"
    return (
        f'<a href="{data_uri}" target="_blank" rel="noopener" title="Abrir foto">'
        f'<img class="thumb" src="{data_uri}" alt="Foto de producto"></a>'
    )


def x__render_image__mutmut_10(image_path: str | None, data_dir: Path | str) -> str:
    path = resolve_image(image_path, data_dir)
    if path is None:
        return f'<div class="placeholder">{PLACEHOLDER_TEXT}</div>'

    mime_type = mimetypes.guess_type(path.name)[1] or "application/octet-stream"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    data_uri = f"data:{mime_type};base64,{encoded}"
    return (
        f'<a href="{data_uri}" target="_blank" rel="noopener" title="Abrir foto">'
        f'<img class="thumb" src="{data_uri}" alt="Foto de producto"></a>'
    )


def x__render_image__mutmut_11(image_path: str | None, data_dir: Path | str) -> str:
    path = resolve_image(image_path, data_dir)
    if path is None:
        return f'<div class="placeholder">{PLACEHOLDER_TEXT}</div>'

    mime_type = mimetypes.guess_type(path.name)[0] or "XXapplication/octet-streamXX"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    data_uri = f"data:{mime_type};base64,{encoded}"
    return (
        f'<a href="{data_uri}" target="_blank" rel="noopener" title="Abrir foto">'
        f'<img class="thumb" src="{data_uri}" alt="Foto de producto"></a>'
    )


def x__render_image__mutmut_12(image_path: str | None, data_dir: Path | str) -> str:
    path = resolve_image(image_path, data_dir)
    if path is None:
        return f'<div class="placeholder">{PLACEHOLDER_TEXT}</div>'

    mime_type = mimetypes.guess_type(path.name)[0] or "APPLICATION/OCTET-STREAM"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    data_uri = f"data:{mime_type};base64,{encoded}"
    return (
        f'<a href="{data_uri}" target="_blank" rel="noopener" title="Abrir foto">'
        f'<img class="thumb" src="{data_uri}" alt="Foto de producto"></a>'
    )


def x__render_image__mutmut_13(image_path: str | None, data_dir: Path | str) -> str:
    path = resolve_image(image_path, data_dir)
    if path is None:
        return f'<div class="placeholder">{PLACEHOLDER_TEXT}</div>'

    mime_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    encoded = None
    data_uri = f"data:{mime_type};base64,{encoded}"
    return (
        f'<a href="{data_uri}" target="_blank" rel="noopener" title="Abrir foto">'
        f'<img class="thumb" src="{data_uri}" alt="Foto de producto"></a>'
    )


def x__render_image__mutmut_14(image_path: str | None, data_dir: Path | str) -> str:
    path = resolve_image(image_path, data_dir)
    if path is None:
        return f'<div class="placeholder">{PLACEHOLDER_TEXT}</div>'

    mime_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    encoded = base64.b64encode(path.read_bytes()).decode(None)
    data_uri = f"data:{mime_type};base64,{encoded}"
    return (
        f'<a href="{data_uri}" target="_blank" rel="noopener" title="Abrir foto">'
        f'<img class="thumb" src="{data_uri}" alt="Foto de producto"></a>'
    )


def x__render_image__mutmut_15(image_path: str | None, data_dir: Path | str) -> str:
    path = resolve_image(image_path, data_dir)
    if path is None:
        return f'<div class="placeholder">{PLACEHOLDER_TEXT}</div>'

    mime_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    encoded = base64.b64encode(None).decode("ascii")
    data_uri = f"data:{mime_type};base64,{encoded}"
    return (
        f'<a href="{data_uri}" target="_blank" rel="noopener" title="Abrir foto">'
        f'<img class="thumb" src="{data_uri}" alt="Foto de producto"></a>'
    )


def x__render_image__mutmut_16(image_path: str | None, data_dir: Path | str) -> str:
    path = resolve_image(image_path, data_dir)
    if path is None:
        return f'<div class="placeholder">{PLACEHOLDER_TEXT}</div>'

    mime_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    encoded = base64.b64encode(path.read_bytes()).decode("XXasciiXX")
    data_uri = f"data:{mime_type};base64,{encoded}"
    return (
        f'<a href="{data_uri}" target="_blank" rel="noopener" title="Abrir foto">'
        f'<img class="thumb" src="{data_uri}" alt="Foto de producto"></a>'
    )


def x__render_image__mutmut_17(image_path: str | None, data_dir: Path | str) -> str:
    path = resolve_image(image_path, data_dir)
    if path is None:
        return f'<div class="placeholder">{PLACEHOLDER_TEXT}</div>'

    mime_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    encoded = base64.b64encode(path.read_bytes()).decode("ASCII")
    data_uri = f"data:{mime_type};base64,{encoded}"
    return (
        f'<a href="{data_uri}" target="_blank" rel="noopener" title="Abrir foto">'
        f'<img class="thumb" src="{data_uri}" alt="Foto de producto"></a>'
    )


def x__render_image__mutmut_18(image_path: str | None, data_dir: Path | str) -> str:
    path = resolve_image(image_path, data_dir)
    if path is None:
        return f'<div class="placeholder">{PLACEHOLDER_TEXT}</div>'

    mime_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    data_uri = None
    return (
        f'<a href="{data_uri}" target="_blank" rel="noopener" title="Abrir foto">'
        f'<img class="thumb" src="{data_uri}" alt="Foto de producto"></a>'
    )

mutants_x__render_image__mutmut['_mutmut_orig'] = x__render_image__mutmut_orig # type: ignore # mutmut generated
mutants_x__render_image__mutmut['x__render_image__mutmut_1'] = x__render_image__mutmut_1 # type: ignore # mutmut generated
mutants_x__render_image__mutmut['x__render_image__mutmut_2'] = x__render_image__mutmut_2 # type: ignore # mutmut generated
mutants_x__render_image__mutmut['x__render_image__mutmut_3'] = x__render_image__mutmut_3 # type: ignore # mutmut generated
mutants_x__render_image__mutmut['x__render_image__mutmut_4'] = x__render_image__mutmut_4 # type: ignore # mutmut generated
mutants_x__render_image__mutmut['x__render_image__mutmut_5'] = x__render_image__mutmut_5 # type: ignore # mutmut generated
mutants_x__render_image__mutmut['x__render_image__mutmut_6'] = x__render_image__mutmut_6 # type: ignore # mutmut generated
mutants_x__render_image__mutmut['x__render_image__mutmut_7'] = x__render_image__mutmut_7 # type: ignore # mutmut generated
mutants_x__render_image__mutmut['x__render_image__mutmut_8'] = x__render_image__mutmut_8 # type: ignore # mutmut generated
mutants_x__render_image__mutmut['x__render_image__mutmut_9'] = x__render_image__mutmut_9 # type: ignore # mutmut generated
mutants_x__render_image__mutmut['x__render_image__mutmut_10'] = x__render_image__mutmut_10 # type: ignore # mutmut generated
mutants_x__render_image__mutmut['x__render_image__mutmut_11'] = x__render_image__mutmut_11 # type: ignore # mutmut generated
mutants_x__render_image__mutmut['x__render_image__mutmut_12'] = x__render_image__mutmut_12 # type: ignore # mutmut generated
mutants_x__render_image__mutmut['x__render_image__mutmut_13'] = x__render_image__mutmut_13 # type: ignore # mutmut generated
mutants_x__render_image__mutmut['x__render_image__mutmut_14'] = x__render_image__mutmut_14 # type: ignore # mutmut generated
mutants_x__render_image__mutmut['x__render_image__mutmut_15'] = x__render_image__mutmut_15 # type: ignore # mutmut generated
mutants_x__render_image__mutmut['x__render_image__mutmut_16'] = x__render_image__mutmut_16 # type: ignore # mutmut generated
mutants_x__render_image__mutmut['x__render_image__mutmut_17'] = x__render_image__mutmut_17 # type: ignore # mutmut generated
mutants_x__render_image__mutmut['x__render_image__mutmut_18'] = x__render_image__mutmut_18 # type: ignore # mutmut generated
mutants_x_main__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_main__mutmut)
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


def x_main__mutmut_orig() -> None:
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


def x_main__mutmut_1() -> None:
    import streamlit as st

    st.set_page_config(page_title=None, layout="wide")
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


def x_main__mutmut_2() -> None:
    import streamlit as st

    st.set_page_config(page_title="Cosmetics", layout=None)
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


def x_main__mutmut_3() -> None:
    import streamlit as st

    st.set_page_config(layout="wide")
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


def x_main__mutmut_4() -> None:
    import streamlit as st

    st.set_page_config(page_title="Cosmetics", )
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


def x_main__mutmut_5() -> None:
    import streamlit as st

    st.set_page_config(page_title="XXCosmeticsXX", layout="wide")
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


def x_main__mutmut_6() -> None:
    import streamlit as st

    st.set_page_config(page_title="cosmetics", layout="wide")
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


def x_main__mutmut_7() -> None:
    import streamlit as st

    st.set_page_config(page_title="COSMETICS", layout="wide")
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


def x_main__mutmut_8() -> None:
    import streamlit as st

    st.set_page_config(page_title="Cosmetics", layout="XXwideXX")
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


def x_main__mutmut_9() -> None:
    import streamlit as st

    st.set_page_config(page_title="Cosmetics", layout="WIDE")
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


def x_main__mutmut_10() -> None:
    import streamlit as st

    st.set_page_config(page_title="Cosmetics", layout="wide")
    st.title(None)

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


def x_main__mutmut_11() -> None:
    import streamlit as st

    st.set_page_config(page_title="Cosmetics", layout="wide")
    st.title("XXInventario de cosméticosXX")

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


def x_main__mutmut_12() -> None:
    import streamlit as st

    st.set_page_config(page_title="Cosmetics", layout="wide")
    st.title("inventario de cosméticos")

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


def x_main__mutmut_13() -> None:
    import streamlit as st

    st.set_page_config(page_title="Cosmetics", layout="wide")
    st.title("INVENTARIO DE COSMÉTICOS")

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


def x_main__mutmut_14() -> None:
    import streamlit as st

    st.set_page_config(page_title="Cosmetics", layout="wide")
    st.title("Inventario de cosméticos")

    only_available = None
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


def x_main__mutmut_15() -> None:
    import streamlit as st

    st.set_page_config(page_title="Cosmetics", layout="wide")
    st.title("Inventario de cosméticos")

    only_available = st.toggle(None, value=True)
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


def x_main__mutmut_16() -> None:
    import streamlit as st

    st.set_page_config(page_title="Cosmetics", layout="wide")
    st.title("Inventario de cosméticos")

    only_available = st.toggle("Solo disponibles", value=None)
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


def x_main__mutmut_17() -> None:
    import streamlit as st

    st.set_page_config(page_title="Cosmetics", layout="wide")
    st.title("Inventario de cosméticos")

    only_available = st.toggle(value=True)
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


def x_main__mutmut_18() -> None:
    import streamlit as st

    st.set_page_config(page_title="Cosmetics", layout="wide")
    st.title("Inventario de cosméticos")

    only_available = st.toggle("Solo disponibles", )
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


def x_main__mutmut_19() -> None:
    import streamlit as st

    st.set_page_config(page_title="Cosmetics", layout="wide")
    st.title("Inventario de cosméticos")

    only_available = st.toggle("XXSolo disponiblesXX", value=True)
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


def x_main__mutmut_20() -> None:
    import streamlit as st

    st.set_page_config(page_title="Cosmetics", layout="wide")
    st.title("Inventario de cosméticos")

    only_available = st.toggle("solo disponibles", value=True)
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


def x_main__mutmut_21() -> None:
    import streamlit as st

    st.set_page_config(page_title="Cosmetics", layout="wide")
    st.title("Inventario de cosméticos")

    only_available = st.toggle("SOLO DISPONIBLES", value=True)
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


def x_main__mutmut_22() -> None:
    import streamlit as st

    st.set_page_config(page_title="Cosmetics", layout="wide")
    st.title("Inventario de cosméticos")

    only_available = st.toggle("Solo disponibles", value=False)
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


def x_main__mutmut_23() -> None:
    import streamlit as st

    st.set_page_config(page_title="Cosmetics", layout="wide")
    st.title("Inventario de cosméticos")

    only_available = st.toggle("Solo disponibles", value=True)
    try:
        rows = None
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


def x_main__mutmut_24() -> None:
    import streamlit as st

    st.set_page_config(page_title="Cosmetics", layout="wide")
    st.title("Inventario de cosméticos")

    only_available = st.toggle("Solo disponibles", value=True)
    try:
        rows = get_inventory(None, only_available=only_available)
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


def x_main__mutmut_25() -> None:
    import streamlit as st

    st.set_page_config(page_title="Cosmetics", layout="wide")
    st.title("Inventario de cosméticos")

    only_available = st.toggle("Solo disponibles", value=True)
    try:
        rows = get_inventory(DB_PATH, only_available=None)
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


def x_main__mutmut_26() -> None:
    import streamlit as st

    st.set_page_config(page_title="Cosmetics", layout="wide")
    st.title("Inventario de cosméticos")

    only_available = st.toggle("Solo disponibles", value=True)
    try:
        rows = get_inventory(only_available=only_available)
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


def x_main__mutmut_27() -> None:
    import streamlit as st

    st.set_page_config(page_title="Cosmetics", layout="wide")
    st.title("Inventario de cosméticos")

    only_available = st.toggle("Solo disponibles", value=True)
    try:
        rows = get_inventory(DB_PATH, )
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


def x_main__mutmut_28() -> None:
    import streamlit as st

    st.set_page_config(page_title="Cosmetics", layout="wide")
    st.title("Inventario de cosméticos")

    only_available = st.toggle("Solo disponibles", value=True)
    try:
        rows = get_inventory(DB_PATH, only_available=only_available)
    except FileNotFoundError:
        st.error(None)
        return
    except sqlite3.Error as exc:
        st.error(f"No se pudo leer la base de datos: {exc}")
        return

    if not rows:
        st.info(EMPTY_MESSAGE)
        return

    st.markdown(render_inventory_table(rows, DATA_DIR), unsafe_allow_html=True)


def x_main__mutmut_29() -> None:
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
        st.error(None)
        return

    if not rows:
        st.info(EMPTY_MESSAGE)
        return

    st.markdown(render_inventory_table(rows, DATA_DIR), unsafe_allow_html=True)


def x_main__mutmut_30() -> None:
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

    if rows:
        st.info(EMPTY_MESSAGE)
        return

    st.markdown(render_inventory_table(rows, DATA_DIR), unsafe_allow_html=True)


def x_main__mutmut_31() -> None:
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
        st.info(None)
        return

    st.markdown(render_inventory_table(rows, DATA_DIR), unsafe_allow_html=True)


def x_main__mutmut_32() -> None:
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

    st.markdown(None, unsafe_allow_html=True)


def x_main__mutmut_33() -> None:
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

    st.markdown(render_inventory_table(rows, DATA_DIR), unsafe_allow_html=None)


def x_main__mutmut_34() -> None:
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

    st.markdown(unsafe_allow_html=True)


def x_main__mutmut_35() -> None:
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

    st.markdown(render_inventory_table(rows, DATA_DIR), )


def x_main__mutmut_36() -> None:
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

    st.markdown(render_inventory_table(None, DATA_DIR), unsafe_allow_html=True)


def x_main__mutmut_37() -> None:
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

    st.markdown(render_inventory_table(rows, None), unsafe_allow_html=True)


def x_main__mutmut_38() -> None:
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

    st.markdown(render_inventory_table(DATA_DIR), unsafe_allow_html=True)


def x_main__mutmut_39() -> None:
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

    st.markdown(render_inventory_table(rows, ), unsafe_allow_html=True)


def x_main__mutmut_40() -> None:
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

    st.markdown(render_inventory_table(rows, DATA_DIR), unsafe_allow_html=False)

mutants_x_main__mutmut['_mutmut_orig'] = x_main__mutmut_orig # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_1'] = x_main__mutmut_1 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_2'] = x_main__mutmut_2 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_3'] = x_main__mutmut_3 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_4'] = x_main__mutmut_4 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_5'] = x_main__mutmut_5 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_6'] = x_main__mutmut_6 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_7'] = x_main__mutmut_7 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_8'] = x_main__mutmut_8 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_9'] = x_main__mutmut_9 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_10'] = x_main__mutmut_10 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_11'] = x_main__mutmut_11 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_12'] = x_main__mutmut_12 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_13'] = x_main__mutmut_13 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_14'] = x_main__mutmut_14 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_15'] = x_main__mutmut_15 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_16'] = x_main__mutmut_16 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_17'] = x_main__mutmut_17 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_18'] = x_main__mutmut_18 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_19'] = x_main__mutmut_19 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_20'] = x_main__mutmut_20 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_21'] = x_main__mutmut_21 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_22'] = x_main__mutmut_22 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_23'] = x_main__mutmut_23 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_24'] = x_main__mutmut_24 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_25'] = x_main__mutmut_25 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_26'] = x_main__mutmut_26 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_27'] = x_main__mutmut_27 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_28'] = x_main__mutmut_28 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_29'] = x_main__mutmut_29 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_30'] = x_main__mutmut_30 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_31'] = x_main__mutmut_31 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_32'] = x_main__mutmut_32 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_33'] = x_main__mutmut_33 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_34'] = x_main__mutmut_34 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_35'] = x_main__mutmut_35 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_36'] = x_main__mutmut_36 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_37'] = x_main__mutmut_37 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_38'] = x_main__mutmut_38 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_39'] = x_main__mutmut_39 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_40'] = x_main__mutmut_40 # type: ignore # mutmut generated


if __name__ == "__main__":
    main()
