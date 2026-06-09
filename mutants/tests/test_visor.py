from __future__ import annotations

import sqlite3
from pathlib import Path

import pytest

from visor import (
    EMPTY_MESSAGE,
    PLACEHOLDER_TEXT,
    connect_read_only,
    format_price,
    get_inventory,
    render_inventory_table,
    resolve_image,
)


SCHEMA = """
CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    brand TEXT NOT NULL,
    name TEXT NOT NULL,
    size TEXT,
    category TEXT
);

CREATE TABLE purchases (
    id INTEGER PRIMARY KEY,
    product_id INTEGER NOT NULL REFERENCES products(id),
    purchase_date DATE NOT NULL,
    price_bob INTEGER NOT NULL,
    finish_date DATE,
    image_path TEXT
);

CREATE VIEW available_products AS
SELECT * FROM purchases WHERE finish_date IS NULL;
"""


def make_db(tmp_path: Path, purchases: list[tuple]) -> Path:
    db_path = tmp_path / "cosmetics.db"
    with sqlite3.connect(db_path) as connection:
        connection.executescript(SCHEMA)
        connection.executemany(
            "INSERT INTO products (id, brand, name, size, category) VALUES (?, ?, ?, ?, ?)",
            [(item[1], item[2], item[3], item[4], None) for item in purchases],
        )
        connection.executemany(
            """
            INSERT INTO purchases (id, product_id, purchase_date, price_bob, finish_date, image_path)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            [(item[0], item[1], item[5], item[6], item[7], item[8]) for item in purchases],
        )
    return db_path


def make_image(tmp_path: Path, relative_path: str = "images/1.jpg") -> Path:
    image_path = tmp_path / relative_path
    image_path.parent.mkdir(parents=True, exist_ok=True)
    image_path.write_bytes(b"fake image bytes")
    return image_path


def test_s1_shows_all_products_with_photo_and_required_fields(tmp_path: Path) -> None:
    make_image(tmp_path, "images/1.jpg")
    make_image(tmp_path, "images/2.jpg")
    make_image(tmp_path, "images/3.jpg")
    db_path = make_db(
        tmp_path,
        [
            (1, 1, "A", "Uno", "10ml", "2026-01-01", 1000, None, "images/1.jpg"),
            (2, 2, "B", "Dos", "20ml", "2026-01-02", 2000, None, "images/2.jpg"),
            (3, 3, "C", "Tres", "30ml", "2026-01-03", 3000, None, "images/3.jpg"),
        ],
    )

    rows = get_inventory(db_path)
    html = render_inventory_table(rows, tmp_path)

    assert len(rows) == 3
    assert html.count("class=\"thumb\"") == 3
    assert "Marca" in html
    assert "Nombre" in html
    assert "Tamaño" in html
    assert "Precio" in html
    assert "Fecha de compra" in html


def test_s2_orders_purchases_by_date_descending(tmp_path: Path) -> None:
    db_path = make_db(
        tmp_path,
        [
            (1, 1, "A", "Enero", None, "2026-01-10", 1000, None, None),
            (2, 2, "B", "Marzo", None, "2026-03-05", 1000, None, None),
            (3, 3, "C", "Febrero", None, "2026-02-01", 1000, None, None),
        ],
    )

    rows = get_inventory(db_path)

    assert rows[0]["purchase_date"] == "2026-03-05"


def test_get_inventory_default_includes_finished_purchases(tmp_path: Path) -> None:
    db_path = make_db(
        tmp_path,
        [
            (1, 1, "A", "Disponible", None, "2026-01-01", 1000, None, None),
            (2, 2, "B", "Terminado", None, "2026-01-02", 1000, "2026-04-30", None),
        ],
    )

    rows = get_inventory(db_path)

    assert len(rows) == 2
    assert {row["finish_date"] for row in rows} == {None, "2026-04-30"}


def test_s3_filters_only_available_from_finish_date(tmp_path: Path) -> None:
    db_path = make_db(
        tmp_path,
        [
            (1, 1, "A", "Uno", None, "2026-01-01", 1000, None, None),
            (2, 2, "B", "Dos", None, "2026-01-02", 1000, None, None),
            (3, 3, "C", "Tres", None, "2026-01-03", 1000, "2026-04-30", None),
        ],
    )

    rows = get_inventory(db_path, only_available=True)

    assert len(rows) == 2
    assert all(row["finish_date"] is None for row in rows)


def test_s4_missing_image_path_renders_placeholder(tmp_path: Path) -> None:
    db_path = make_db(
        tmp_path,
        [(1, 1, "A", "Uno", None, "2026-01-01", 1000, None, None)],
    )

    rows = get_inventory(db_path)
    html = render_inventory_table(rows, tmp_path)

    assert resolve_image(None, tmp_path) is None
    assert PLACEHOLDER_TEXT in html


def test_s5_broken_image_path_renders_placeholder(tmp_path: Path) -> None:
    db_path = make_db(
        tmp_path,
        [(1, 1, "A", "Uno", None, "2026-01-01", 1000, None, "images/999.jpg")],
    )

    rows = get_inventory(db_path)
    html = render_inventory_table(rows, tmp_path)

    assert resolve_image("images/999.jpg", tmp_path) is None
    assert PLACEHOLDER_TEXT in html


def test_s6_empty_inventory_returns_no_rows_for_empty_message(tmp_path: Path) -> None:
    db_path = make_db(tmp_path, [])

    rows = get_inventory(db_path)

    assert rows == []
    assert EMPTY_MESSAGE == "No hay productos cargados"


def test_s7_missing_database_raises_clear_error_without_creating_file(tmp_path: Path) -> None:
    db_path = tmp_path / "missing.db"


    with pytest.raises(FileNotFoundError, match="No existe la base de datos esperada"):
        get_inventory(db_path)

    assert not db_path.exists()


def test_s8_database_connection_is_read_only(tmp_path: Path) -> None:
    db_path = make_db(
        tmp_path,
        [(1, 1, "A", "Uno", None, "2026-01-01", 1000, None, None)],
    )

    with connect_read_only(db_path) as connection:
        with pytest.raises(sqlite3.OperationalError):
            connection.execute(
                "INSERT INTO products (id, brand, name) VALUES (99, 'X', 'Y')"
            )


def test_connect_read_only_uses_sqlite_uri_mode_ro(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    db_path = tmp_path / "cosmetics.db"
    db_path.write_bytes(b"")
    call = {}

    def fake_connect(*args, **kwargs):
        call["args"] = args
        call["kwargs"] = kwargs
        return object()

    monkeypatch.setattr(sqlite3, "connect", fake_connect)

    connect_read_only(db_path)

    assert call == {
        "args": (f"file:{db_path.resolve().as_posix()}?mode=ro",),
        "kwargs": {"uri": True},
    }


def test_render_inventory_table_escapes_fields_and_embeds_clickable_images(tmp_path: Path) -> None:
    make_image(tmp_path, "images/1.jpg")
    make_image(tmp_path, "images/2.jpg")
    rows = [
        {
            "brand": "A&B",
            "name": "<Serum>",
            "size": "30ml",
            "price_bob": 1234,
            "purchase_date": "2026-01-02",
            "finish_date": None,
            "image_path": "images/1.jpg",
        },
        {
            "brand": "C",
            "name": "Cream",
            "size": "50ml",
            "price_bob": 2000,
            "purchase_date": "2026-01-01",
            "finish_date": "2026-04-30",
            "image_path": "images/2.jpg",
        },
    ]

    html = render_inventory_table(rows, tmp_path)

    assert "XXXX" not in html
    assert html.count("class=\"thumb\"") == 2
    assert "data:image/jpeg;base64,ZmFrZSBpbWFnZSBieXRlcw==" in html
    assert "data:None" not in html
    assert 'target="_blank" rel="noopener" title="Abrir foto"' in html
    assert "<td>A&amp;B</td>" in html
    assert "<td>&lt;Serum&gt;</td>" in html
    assert "<td>30ml</td>" in html
    assert "<td>Bs 12.34</td>" in html
    assert "<td>2026-01-02</td>" in html
    assert "<td>2026-04-30</td>" in html


def test_s9_formats_price_from_cents() -> None:
    assert format_price(24600) == "Bs 246.00"
