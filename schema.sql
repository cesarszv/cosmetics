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
