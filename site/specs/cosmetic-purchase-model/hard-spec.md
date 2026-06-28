# Hard Spec: Cosmetic Purchase Model

Estado: hard-spec-needed

Fuente: `spec.md`

## Requisitos verificables

- R1: `cosmetic_purchases` en `database/schema.sql` con exactamente 15 columnas: id, brand, product_name, category, product_type, size_value, size_unit, purchase_date, price_bob_cents, ended_date, ended_date_kind, image_path, notes, created_at, updated_at.
- R2: `id` INTEGER PRIMARY KEY.
- R3: `brand` TEXT NOT NULL.
- R4: `product_name` TEXT NOT NULL.
- R5: `category` TEXT NOT NULL con CHECK enum skincare, haircare, lipcare.
- R6: `product_type` TEXT NOT NULL con CHECK enum sunscreen, moisturizer, treatment, serum, conditioner, lip_balm, leave_in.
- R7: `size_value` REAL nullable con CHECK `size_value IS NULL OR size_value > 0`.
- R8: `size_unit` TEXT nullable con CHECK enum ml, g, unit.
- R9: `purchase_date` TEXT NOT NULL con CHECK `GLOB '????-??-??'`.
- R10: `price_bob_cents` INTEGER NOT NULL con CHECK `>= 0`.
- R11: `ended_date` TEXT nullable con CHECK `GLOB '????-??-??'` y CHECK `ended_date IS NULL OR ended_date >= purchase_date`.
- R12: `ended_date_kind` TEXT nullable con CHECK enum exact, estimated.
- R13: `image_path` TEXT nullable, relativo a `database/data/`.
- R14: `notes` TEXT nullable.
- R15: `created_at` TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP.
- R16: `updated_at` TEXT nullable.
- R17: `idx_cosmetic_purchases_purchase_date` sobre `(purchase_date DESC, id DESC)`.
- R18: `idx_cosmetic_purchases_ended_date` sobre `(ended_date)`.
- R19: `idx_cosmetic_purchases_category` sobre `(category)`.
- R20: view `current_inventory` retorna filas con `ended_date IS NULL`.
- R21: view `purchase_history` retorna todas las filas ORDER BY `purchase_date DESC, id DESC`.
- R22: view `skincare_spending` agrupa por `product_type` con `COUNT(*)` y `SUM(price_bob_cents)` filtrando `category = 'skincare'`.

## Reglas verificables

- V1: No columna `available`; el validador raisea si la encuentra.
- V2: Paired-null: `ended_date` y `ended_date_kind` deben ser ambos NULL o ambos non-NULL (CHECK constraint).
- V3: Dinero como integer cents (BOB), nunca floats.
- V4: Fechas como TEXT ISO `YYYY-MM-DD` con GLOB `????-??-??'`, no tipo DATE.
- V5: `ended_date >= purchase_date` por CHECK (lexicografico, valido por ISO ordering).
- V6: Tabla intencionalmente denormalizada: sin foreign keys, sin tablas marca/producto, brand y product_name free-text.
- V7: Sin migraciones; snapshots `.before-*` como historia.

## Casos limite

- C1: `NULL ended_date` + `NULL ended_date_kind` = disponible/en uso (unica forma de ser current).
- C2: `ended_date_kind = 'estimated'` vs `'exact'`: ambos validos; solo `estimated` genera "(estimada)" en UI.
- C3: `image_path = NULL` valido; UI muestra placeholder "Sin foto".
- C4: `size_value` y `size_unit` nullable independientes — sin paired-null.
- C5: `price_bob_cents = 0` valido, renderiza `Bs 0.00`.
- C6: `ended_date = purchase_date` valido (>=, no >).
- C7: GLOB `????-??-??'` valida forma, no calendario (`2026-13-45` pasa).
- C8: `notes` y `updated_at` se almacenan pero ningun consumidor los lee.

## No requisitos

- N1: No columna `available` (derivar de `ended_date IS NULL`).
- N2: No paired-null para `size_value`/`size_unit`.
- N3: No foreign keys, no triggers, no unicidad mas alla de PK.
- N4: No cota "no futuro" para fechas; no cota superior para price.
- N5: No moneda distinta a BOB; no conversion; solo integer cents.
- N6: `notes` y `updated_at` write-only (sin consumidor).
- N7: GLOB y enums son schema-only — el validador no los re-chequea.

## Preguntas pendientes

- TBD: `updated_at` sin maintainer — mantener o remover.
- TBD: `notes` con datos pero sin render en UI — surfacear o no.
- TBD: views sin consumidor — surfacear `skincare_spending` o no.
- TBD: `size_unit = 'unit'` permitido pero no usado en datos actuales.
