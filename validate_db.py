from __future__ import annotations

import sqlite3
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent
DATA_DIR = PROJECT_ROOT / "data"
DB_PATH = DATA_DIR / "cosmetics.db"


REQUIRED_COLUMNS = {
    "id",
    "brand",
    "product_name",
    "category",
    "product_type",
    "size_value",
    "size_unit",
    "purchase_date",
    "price_bob_cents",
    "ended_date",
    "ended_date_kind",
    "image_path",
    "notes",
    "created_at",
    "updated_at",
}


def main() -> None:
    if not DB_PATH.exists():
        raise FileNotFoundError(f"No existe la base esperada: {DB_PATH}")

    with sqlite3.connect(DB_PATH) as connection:
        connection.row_factory = sqlite3.Row
        validate_integrity(connection)
        validate_schema(connection)
        validate_rows(connection)
        print_summary(connection)


def validate_integrity(connection: sqlite3.Connection) -> None:
    result = connection.execute("PRAGMA integrity_check").fetchone()[0]
    if result != "ok":
        raise RuntimeError(f"SQLite integrity_check falló: {result}")


def validate_schema(connection: sqlite3.Connection) -> None:
    tables = {
        row["name"]
        for row in connection.execute(
            "SELECT name FROM sqlite_master WHERE type = 'table'"
        )
    }
    if "cosmetic_purchases" not in tables:
        raise RuntimeError("Falta la tabla cosmetic_purchases")

    columns = {
        row["name"]
        for row in connection.execute("PRAGMA table_info(cosmetic_purchases)")
    }
    missing = REQUIRED_COLUMNS - columns
    if missing:
        raise RuntimeError(f"Faltan columnas en cosmetic_purchases: {sorted(missing)}")

    if "available" in columns:
        raise RuntimeError("No debe existir columna available; usá ended_date")


def validate_rows(connection: sqlite3.Connection) -> None:
    checks = {
        "fechas ended_date/ended_date_kind inconsistentes": """
            SELECT COUNT(*)
            FROM cosmetic_purchases
            WHERE (ended_date IS NULL AND ended_date_kind IS NOT NULL)
               OR (ended_date IS NOT NULL AND ended_date_kind IS NULL)
        """,
        "productos terminados antes de compra": """
            SELECT COUNT(*)
            FROM cosmetic_purchases
            WHERE ended_date IS NOT NULL
              AND ended_date < purchase_date
        """,
        "precios negativos": """
            SELECT COUNT(*)
            FROM cosmetic_purchases
            WHERE price_bob_cents < 0
        """,
        "tamaños inválidos": """
            SELECT COUNT(*)
            FROM cosmetic_purchases
            WHERE size_value IS NOT NULL
              AND size_value <= 0
        """,
    }

    for label, query in checks.items():
        count = connection.execute(query).fetchone()[0]
        if count:
            raise RuntimeError(f"Hay {count} filas con {label}")

    missing_images = [
        row["image_path"]
        for row in connection.execute(
            """
            SELECT image_path
            FROM cosmetic_purchases
            WHERE image_path IS NOT NULL
            """
        )
        if not (DATA_DIR / row["image_path"]).is_file()
    ]
    if missing_images:
        raise RuntimeError(f"Faltan imágenes referenciadas: {missing_images}")


def print_summary(connection: sqlite3.Connection) -> None:
    total = connection.execute("SELECT COUNT(*) FROM cosmetic_purchases").fetchone()[0]
    current = connection.execute(
        "SELECT COUNT(*) FROM cosmetic_purchases WHERE ended_date IS NULL"
    ).fetchone()[0]
    ended = connection.execute(
        "SELECT COUNT(*) FROM cosmetic_purchases WHERE ended_date IS NOT NULL"
    ).fetchone()[0]
    estimated = connection.execute(
        "SELECT COUNT(*) FROM cosmetic_purchases WHERE ended_date_kind = 'estimated'"
    ).fetchone()[0]

    print("DB válida")
    print(f"Compras: {total}")
    print(f"Actuales: {current}")
    print(f"Terminadas/no disponibles: {ended}")
    print(f"Fechas estimadas: {estimated}")


if __name__ == "__main__":
    main()
