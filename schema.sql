CREATE TABLE cosmetic_purchases (
    id INTEGER PRIMARY KEY,
    brand TEXT NOT NULL,
    product_name TEXT NOT NULL,
    category TEXT NOT NULL,
    product_type TEXT NOT NULL,
    size_value REAL,
    size_unit TEXT,
    purchase_date TEXT NOT NULL,
    price_bob_cents INTEGER NOT NULL,
    ended_date TEXT,
    ended_date_kind TEXT,
    image_path TEXT,
    notes TEXT,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT,

    CHECK (category IN ('skincare', 'haircare', 'lipcare')),
    CHECK (product_type IN ('sunscreen', 'moisturizer', 'treatment', 'serum', 'conditioner', 'lip_balm', 'leave_in')),
    CHECK (size_value IS NULL OR size_value > 0),
    CHECK (size_unit IS NULL OR size_unit IN ('ml', 'g', 'unit')),
    CHECK (purchase_date GLOB '????-??-??'),
    CHECK (price_bob_cents >= 0),
    CHECK (ended_date IS NULL OR ended_date GLOB '????-??-??'),
    CHECK (ended_date_kind IS NULL OR ended_date_kind IN ('exact', 'estimated')),
    CHECK (
        (ended_date IS NULL AND ended_date_kind IS NULL)
        OR (ended_date IS NOT NULL AND ended_date_kind IS NOT NULL)
    ),
    CHECK (ended_date IS NULL OR ended_date >= purchase_date)
);

CREATE INDEX idx_cosmetic_purchases_purchase_date
ON cosmetic_purchases (purchase_date DESC, id DESC);

CREATE INDEX idx_cosmetic_purchases_ended_date
ON cosmetic_purchases (ended_date);

CREATE INDEX idx_cosmetic_purchases_category
ON cosmetic_purchases (category);

CREATE VIEW current_inventory AS
SELECT *
FROM cosmetic_purchases
WHERE ended_date IS NULL;

CREATE VIEW purchase_history AS
SELECT *
FROM cosmetic_purchases
ORDER BY purchase_date DESC, id DESC;

CREATE VIEW skincare_spending AS
SELECT
    product_type,
    COUNT(*) AS purchase_count,
    SUM(price_bob_cents) AS total_bob_cents
FROM cosmetic_purchases
WHERE category = 'skincare'
GROUP BY product_type;
