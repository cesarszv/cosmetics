# Hard Spec: DB Validation

Estado: hard-spec-needed

Fuente: `spec.md`

## Requisitos verificables

- R1: `DB_PATH` hardcoded a `PROJECT_ROOT/database/data/cosmetics.db`.
- R2: DB inexistente raisea `FileNotFoundError` con "No existe la base esperada".
- R3: `REQUIRED_COLUMNS` es exactamente {id, brand, product_name, category, product_type, size_value, size_unit, purchase_date, price_bob_cents, ended_date, ended_date_kind, image_path, notes, created_at, updated_at} (15 columnas).
- R4: `print_summary` imprime "DB valida" + Compras, Actuales, Terminadas/no disponibles, Fechas estimadas.
- R5: "Actuales" = filas con `ended_date IS NULL`.
- R6: "Terminadas/no disponibles" = filas con `ended_date IS NOT NULL`.
- R7: "Fechas estimadas" = filas con `ended_date_kind = 'estimated'`.

## Reglas verificables

- V1: `PRAGMA integrity_check` debe retornar "ok"; si no, RuntimeError.
- V2: `cosmetic_purchases` debe existir en `sqlite_master`; si no, RuntimeError.
- V3: Set de columnas debe coincidir exactamente con `REQUIRED_COLUMNS`; si faltan, RuntimeError.
- V4: Columna `available` presente -> RuntimeError con "No debe existir columna available; usa ended_date".
- V5: Paired-null: cuenta filas inconsistentes ended_date/ended_date_kind; si >0, RuntimeError.
- V6: Date order: cuenta filas con `ended_date < purchase_date`; si >0, RuntimeError.
- V7: Price: cuenta filas con `price_bob_cents < 0`; si >0, RuntimeError.
- V8: Size: cuenta filas con `size_value <= 0` (si presente); si >0, RuntimeError.
- V9: Referenced images: cada `image_path` no-NULL debe apuntar a archivo existente; si falta, RuntimeError.
- V10: Cualquier fallo raisea (short-circuit); solo run all-pass llega a `print_summary`.

## Casos limite

- C1: Row-check fallido usa count en mensaje ("Hay {count} filas con ...").
- C2: Missing-image check corre despues de los cuatro row-count checks.
- C3: Image check resuelve contra `DATA_DIR` hardcoded, no parametro.

## No requisitos

- N1: No parameterizable: `DB_PATH` y `DATA_DIR` constantes module-level; `main()` sin args.
- N2: No valida GLOB date format — confia en schema CHECK.
- N3: No valida enum membership — confia en schema CHECK.
- N4: No valida paired-null de `size_value`/`size_unit`.
- N5: No conexion read-only (`sqlite3.connect` normal).
- N6: No valida `purchase_date` presence/format mas alla del schema.
- N7: No test file dedicado.

## Preguntas pendientes

- TBD: `validate_db.py` sin tests — no unit-testeable sin refactor (DB_PATH hardcoded).
- TBD: `product_type` enum solo enforced a SQLite CHECK, validador no lo chequea.
