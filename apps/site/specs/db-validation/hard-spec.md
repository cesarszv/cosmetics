# Hard Spec: DB Validation

Estado: hard-spec-needed

Fuente: `spec.md`

## Requisitos verificables

- R1: `DB_PATH` es hardcoded a `PROJECT_ROOT/database/data/cosmetics.db`.
- R2: Si la DB no existe, raisea `FileNotFoundError` con mensaje "No existe la base esperada".
- R3: `REQUIRED_COLUMNS` es exactamente {id, brand, product_name, category, product_type, size_value, size_unit, purchase_date, price_bob_cents, ended_date, ended_date_kind, image_path, notes, created_at, updated_at} (15 columnas).
- R4: `print_summary` imprime "DB valida" seguido de Compras, Actuales, Terminadas/no disponibles, Fechas estimadas.
- R5: "Actuales" cuenta filas donde `ended_date IS NULL`.
- R6: "Terminadas/no disponibles" cuenta filas donde `ended_date IS NOT NULL`.
- R7: "Fechas estimadas" cuenta filas donde `ended_date_kind = 'estimated'`.

## Reglas verificables

- V1: `PRAGMA integrity_check` debe retornar "ok"; si no, raisea RuntimeError.
- V2: La tabla `cosmetic_purchases` debe existir en `sqlite_master`; si no, raisea RuntimeError.
- V3: El set de columnas debe coincidir exactamente con `REQUIRED_COLUMNS`; si faltan, raisea RuntimeError.
- V4: Si existe columna `available`, raisea RuntimeError con mensaje "No debe existir columna available; usa ended_date".
- V5: Paired-null: cuenta filas donde ended_date/ended_date_kind son inconsistentes; si >0, raisea RuntimeError.
- V6: Date order: cuenta filas donde `ended_date < purchase_date`; si >0, raisea RuntimeError.
- V7: Price: cuenta filas donde `price_bob_cents < 0`; si >0, raisea RuntimeError.
- V8: Size: cuenta filas donde `size_value <= 0` (si presente); si >0, raisea RuntimeError.
- V9: Referenced images: verifica que cada `image_path` no-NULL apunte a archivo existente; si falta, raisea RuntimeError.
- V10: Cualquier fallo raisea (short-circuit); solo un run all-pass llega a `print_summary`.

## Casos limite

- C1: Un row-check que falla usa el count en el mensaje ("Hay {count} filas con ...").
- C2: Missing-image check corre despues de los cuatro row-count checks.
- C3: Image check resuelve contra `DATA_DIR` hardcoded, no un parametro.

## No requisitos

- N1: No parameterizable: `DB_PATH` y `DATA_DIR` son constantes module-level; `main()` no toma args.
- N2: No valida GLOB date format — confia en schema CHECK.
- N3: No valida enum membership — confia en schema CHECK.
- N4: No valida paired-null de `size_value`/`size_unit`.
- N5: No usa conexion read-only (usa `sqlite3.connect` normal).
- N6: No valida `purchase_date` presence/format mas alla del schema.
- N7: No tiene test file dedicado.

## Preguntas pendientes

- TBD: `validate_db.py` no tiene tests — no es unit-testeable sin refactor (DB_PATH hardcoded).
- TBD: `product_type` enum solo enforced a SQLite CHECK, validador no lo chequea explicitamente.
