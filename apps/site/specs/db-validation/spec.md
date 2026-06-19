---
title: DB Validation
status: draft
description: Validador de integridad de la DB antes de generar/publicar el sitio, CI gate fail-fast
---

# Spec: DB Validation

## Intencion

Validar integridad de la DB antes de generar o publicar el sitio. CI gate — si falla, el build no procede.

## Contexto

- `apps/site/validate_db.py` — validador (138 lineas)
- `database/schema.sql` — esquema esperado
- `database/data/cosmetics.db` — DB a validar
- VSCode task `check` encadena validate-db a pytest
- Relacionada con: `cosmetic-purchase-model`, `static-inventory-dashboard`

## Conceptos principales

### integrity_check

SQLite `PRAGMA integrity_check`.

### Schema presence

Verifica que `cosmetic_purchases` exista.

### Column set

Verifica el set exacto de columnas.

### No available column

RAISEA si encuentra columna `available` (ver `cosmetic-purchase-model`).

### Date consistency

`ended_date >= purchase_date`, formato GLOB `????-??-??'`.

### Paired-null

`ended_date` y `ended_date_kind` ambos NULL o ambos non-NULL.

### Price/size constraints

`price_bob_cents >= 0`, `size_value > 0` si presente.

### Image existence

Imagenes referenciadas existen en `database/data/`.

### Output

Imprime counts (Compras/Actuales/Terminadas/Fechas estimadas) o raisea.

## Principios

- Fail-fast: raisea `RuntimeError` con mensaje descriptivo
- No parameterizable — `DB_PATH` hardcoded (a diferencia de `build.py`)
- Corre antes de pytest en el task `check`

## Alcance

- `validate_db.py` — validacion de integridad, schema, datos

## Fuera de alcance

- Generacion del sitio (ver `static-inventory-dashboard`)
- Deploy (ver `site-deploy`)
- Tests unitarios del validador

## Preguntas pendientes

- TBD: `validate_db.py` sin tests — no unit-testeable sin refactor (DB_PATH hardcoded, sin override).
- TBD: `product_type` enum solo enforced a SQLite CHECK, validador no lo chequea.
