from __future__ import annotations

import sqlite3
from pathlib import Path

import pytest

from build import (
    EMPTY_MESSAGE,
    PLACEHOLDER_TEXT,
    build_site,
    connect_read_only,
    format_price,
    get_inventory,
    prepare_rows,
    render_document,
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


def test_s1_reads_all_products_with_required_fields_and_images(tmp_path: Path) -> None:
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
    prepared, copied = prepare_rows(rows, tmp_path, tmp_path / "dist/images")
    html = render_document(prepared)

    assert len(rows) == 3
    assert copied == 3
    assert "Marca" not in html
    assert "Uno" in html
    assert "10ml" in html
    assert "Bs 10.00" in html
    assert "2026-01-01" in html


def test_s2_orders_purchases_by_date_descending_and_id_descending(tmp_path: Path) -> None:
    db_path = make_db(
        tmp_path,
        [
            (1, 1, "A", "Enero", None, "2026-01-10", 1000, None, None),
            (2, 2, "B", "Marzo viejo", None, "2026-03-05", 1000, None, None),
            (3, 3, "C", "Febrero", None, "2026-02-01", 1000, None, None),
            (4, 4, "D", "Marzo nuevo", None, "2026-03-05", 1000, None, None),
        ],
    )

    rows = get_inventory(db_path)

    assert rows[0]["purchase_id"] == 4
    assert rows[1]["purchase_id"] == 2


def test_s3_available_is_derived_from_finish_date(tmp_path: Path) -> None:
    db_path = make_db(
        tmp_path,
        [
            (1, 1, "A", "Uno", None, "2026-01-01", 1000, None, None),
            (2, 2, "B", "Dos", None, "2026-01-02", 1000, None, None),
            (3, 3, "C", "Tres", None, "2026-01-03", 1000, "2026-04-30", None),
        ],
    )

    prepared, _ = prepare_rows(get_inventory(db_path), tmp_path, tmp_path / "dist/images")

    assert [row["available"] for row in prepared] == [False, True, True]


def test_s4_missing_image_path_renders_placeholder(tmp_path: Path) -> None:
    db_path = make_db(
        tmp_path,
        [(1, 1, "A", "Uno", None, "2026-01-01", 1000, None, None)],
    )

    prepared, copied = prepare_rows(get_inventory(db_path), tmp_path, tmp_path / "dist/images")
    html = render_document(prepared)

    assert copied == 0
    assert resolve_image(None, tmp_path) is None
    assert PLACEHOLDER_TEXT in html


def test_s5_broken_image_path_renders_placeholder(tmp_path: Path) -> None:
    db_path = make_db(
        tmp_path,
        [(1, 1, "A", "Uno", None, "2026-01-01", 1000, None, "images/999.jpg")],
    )

    prepared, copied = prepare_rows(get_inventory(db_path), tmp_path, tmp_path / "dist/images")
    html = render_document(prepared)

    assert copied == 0
    assert resolve_image("images/999.jpg", tmp_path) is None
    assert PLACEHOLDER_TEXT in html


def test_s6_empty_inventory_generates_empty_state(tmp_path: Path) -> None:
    db_path = make_db(tmp_path, [])

    prepared, copied = prepare_rows(get_inventory(db_path), tmp_path, tmp_path / "dist/images")
    html = render_document(prepared)

    assert prepared == []
    assert copied == 0
    assert EMPTY_MESSAGE in html


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


def test_s9_formats_price_from_cents() -> None:
    assert format_price(24600) == "Bs 246.00"


def test_generated_html_escapes_fields_safely(tmp_path: Path) -> None:
    rows = [
        {
            "purchase_id": 1,
            "brand": "A&B",
            "name": "</script><img src=x onerror=alert(1)>",
            "size": "30ml",
            "price_bob": 1234,
            "purchase_date": "2026-01-02",
            "finish_date": None,
            "image_path": None,
        }
    ]

    prepared, _ = prepare_rows(rows, tmp_path, tmp_path / "dist/images")
    html = render_document(prepared)

    assert "A&amp;B" in html
    assert "&lt;/script&gt;&lt;img" in html
    assert "</script><img" not in html


def test_image_paths_cannot_escape_data_directory(tmp_path: Path) -> None:
    outside = tmp_path.parent / "outside.jpg"
    outside.write_bytes(b"outside")

    assert resolve_image("../outside.jpg", tmp_path) is None


def test_build_site_writes_index_and_copies_only_referenced_images(tmp_path: Path) -> None:
    make_image(tmp_path, "images/1.jpg")
    make_image(tmp_path, "images/unused.jpg")
    db_path = make_db(
        tmp_path,
        [(1, 1, "A", "Uno", "10ml", "2026-01-01", 1000, None, "images/1.jpg")],
    )
    dist_dir = tmp_path / "dist"

    result = build_site(db_path=db_path, data_dir=tmp_path, dist_dir=dist_dir)

    assert result.output_file == dist_dir / "index.html"
    assert result.rows == 1
    assert result.copied_images == 1
    assert (dist_dir / "index.html").is_file()
    assert (dist_dir / ".nojekyll").is_file()
    assert (dist_dir / "images" / "purchase-1.jpg").is_file()
    assert not (dist_dir / "images" / "unused.jpg").exists()


def test_static_ui_defaults_to_only_available_filter() -> None:
    html = render_document([])

    assert '<input id="availableOnly" type="checkbox" checked>' in html


def test_generator_has_no_streamlit_or_pandas_runtime_dependency() -> None:
    source = Path("build.py").read_text(encoding="utf-8")

    assert "streamlit" not in source
    assert "pandas" not in source
