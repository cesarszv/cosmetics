# Hard Spec: Cosmetic Purchase Model

Estado: hard-spec-needed

Fuente: `spec.md`

## Requisitos verificables

- R1: La tabla `cosmetic_purchases` existe en `database/schema.sql` con exactamente 15 columnas: id, brand, product_name, category, product_type, size_value, size_unit, purchase_date, price_bob_cents, ended_date, ended_date_kind, image_path, notes, created_at, updated_at.
- R2: `id` es INTEGER PRIMARY KEY.
- R3: `brand` es TEXT NOT NULL.
- R4: `product_name` es TEXT NOT NULL.
- R5: `category` es TEXT NOT NULL con CHECK enum de skincare, haircare, lipcare.
- R6: `product_type` es TEXT NOT NULL con CHECK enum de sunscreen, moisturizer, treatment, serum, conditioner, lip_balm, leave_in.
- R7: `size_value` es REAL nullable con CHECK `size_value IS NULL OR size_value > 0`.
- R8: `size_unit` es TEXT nullable con CHECK enum de ml, g, unit.
- R9: `purchase_date` es TEXT NOT NULL con CHECK `GLOB '????-??-??'`.
- R10: `price_bob_cents` es INTEGER NOT NULL con CHECK `>= 0`.
- R11: `ended_date` es TEXT nullable con CHECK `GLOB '????-??-??'` y CHECK `ended_date IS NULL OR ended_date >= purchase_date`.
- R12: `ended_date_kind` es TEXT nullable con CHECK enum de exact, estimated.
- R13: `image_path` es TEXT nullable, relativo a `database/data/`.
- R14: `notes` es TEXT nullable.
- R15: `created_at` es TEXT NOT NULL con DEFAULT CURRENT_TIMESTAMP.
- R16: `updated_at` es TEXT nullable.
- R17: El indice `idx_cosmetic_purchases_purchase_date` existe sobre `(purchase_date DESC, id DESC)`.
- R18: El indice `idx_cosmetic_purchases_ended_date` existe sobre `(ended_date)`.
- R19: El indice `idx_cosmetic_purchases_category` existe sobre `(category)`.
- R20: La view `current_inventory` retorna filas donde `ended_date IS NULL`.
- R21: La view `purchase_history` retorna todas las filas ordenadas por `purchase_date DESC, id DESC`.
- R22: La view `skincare_spending` agrupa por `product_type` con `COUNT(*)` y `SUM(price_bob_cents)` filtrando `category = 'skincare'`.

## Reglas verificables

- V1: No existe columna `available` en el schema. El validador raisea si la encuentra.
- V2: Paired-null: `ended_date` y `ended_date_kind` deben ser ambos NULL o ambos non-NULL (CHECK constraint).
- V3: El dinero se guarda como integer cents (BOB), nunca como floats.
- V4: Las fechas se guardan como TEXT ISO `YYYY-MM-DD` con GLOB `????-??-??'`, no como tipo DATE.
- V5: `ended_date >= purchase_date` se enforcea por CHECK (string comparison lexicografico, valido porque ISO dates ordenan correctamente).
- V6: La tabla es intencionalmente denormalizada: sin foreign keys, sin tablas de marca/producto, brand y product_name son free-text.
- V7: Sin framework de migraciones; snapshots `.before-*` como marcadores de historia.

## Casos limite

- C1: `NULL ended_date` + `NULL ended_date_kind` significa disponible/en uso (unica forma de ser current).
- C2: `ended_date_kind = 'estimated'` vs `'exact'`: ambos permitidos; solo `estimated` genera el sufijo "(estimada)" en la UI.
- C3: `image_path = NULL` es valido; la UI muestra placeholder "Sin foto".
- C4: `size_value` y `size_unit` son independientemente nullable — no hay paired-null para size.
- C5: `price_bob_cents = 0` es valido (>= 0), renderiza `Bs 0.00`.
- C6: `ended_date = purchase_date` es valido (>=, no >).
- C7: `GLOB '????-??-??'` valida forma, no validez calendario (`2026-13-45` pasa el CHECK).
- C8: `notes` y `updated_at` se almacenan pero ningun consumidor los lee.

## No requisitos

- N1: No columna `available` (disponibilidad derivada de `ended_date IS NULL`).
- N2: No paired-null constraint para `size_value`/`size_unit`.
- N3: No foreign keys, no triggers, no unicidad mas alla de PK.
- N4: No cota "no en el futuro" para `purchase_date`/`ended_date`; no cota superior para price.
- N5: No moneda distinta a BOB; no conversion; solo integer cents.
- N6: `notes` y `updated_at` son write-only desde el pipeline (sin consumidor).
- N7: GLOB y enums son schema-only — el validador no los re-chequea.

## Preguntas pendientes

- TBD: `updated_at` declarado pero sin maintainer — decidir mantener o remover.
- TBD: `notes` con datos pero sin render en UI — decidir surfacear.
- TBD: views sin consumidor en el sitio — decidir surfacear `skincare_spending`.
- TBD: `size_unit = 'unit'` permitido pero no usado en datos actuales.
