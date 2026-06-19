---
title: Cosmetic Purchase Model
status: draft
description: Modelo de dominio de la compra de cosmetico, la tabla unica que la almacena, sus invariantes y reglas de derivacion
---

# Spec: Cosmetic Purchase Model

## Intencion

Definir que es una compra de cosmetico como entidad de dominio, la tabla unica que la almacena, sus invariantes y reglas de derivacion. Es la spec canonica del modelo; `static-inventory-dashboard` la consume al renderizar y `db-validation` la respeta al validar.

## Contexto

- `database/schema.sql` — esquema versionado de SQLite (tabla, 3 indices, 3 views)
- `database/data/cosmetics.db` — DB local, source of truth
- `apps/site/build.py` — implementacion que consume el modelo
- `apps/site/validate_db.py` — validador que enforcea las reglas

## Conceptos principales

### Tabla cosmetic_purchases

Una fila = una unidad comprada. Sin tablas separadas de producto/marca (brand y product_name son free-text). Columnas:
- id (INTEGER PRIMARY KEY)
- brand (TEXT NOT NULL)
- product_name (TEXT NOT NULL)
- category (TEXT NOT NULL, enum: skincare/haircare/lipcare)
- product_type (TEXT NOT NULL, enum: sunscreen/moisturizer/treatment/serum/conditioner/lip_balm/leave_in)
- size_value (REAL nullable, >0 si presente)
- size_unit (TEXT nullable, enum: ml/g/unit)
- purchase_date (TEXT NOT NULL, ISO YYYY-MM-DD con GLOB)
- price_bob_cents (INTEGER NOT NULL, >=0)
- ended_date (TEXT nullable, ISO, >= purchase_date)
- ended_date_kind (TEXT nullable, enum: exact/estimated)
- image_path (TEXT nullable, relativo a database/data/)
- notes (TEXT nullable)
- created_at (TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP)
- updated_at (TEXT nullable, declarado pero sin maintainer)

### Indices

- idx_cosmetic_purchases_purchase_date (purchase_date DESC, id DESC)
- idx_cosmetic_purchases_ended_date (ended_date)
- idx_cosmetic_purchases_category (category)

### Views

- current_inventory (WHERE ended_date IS NULL)
- purchase_history (all rows ORDER BY purchase_date DESC)
- skincare_spending (per product_type count + SUM para skincare)
- NOTA: las views existen en schema pero el sitio no las usa; lee la tabla base directamente

### Relaciones

Intencionalmente denormalizada, sin foreign keys, identidad de marca/producto por string equality

## Principios

- Disponibilidad derivada: no existe columna `available`; se deriva de `ended_date IS NULL`. El validador RAISEA si encuentra una columna `available`.
- Paired-null: `ended_date` y `ended_date_kind` deben ser ambos NULL o ambos non-NULL (CHECK constraint + validador)
- Money como integer cents (BOB), nunca floats. `format_price` divide por 100.
- Fechas como ISO `YYYY-MM-DD` TEXT con GLOB `????-??-??'` (no tipo DATE — depende de string ordering)
- `ended_date_kind` distingue fechas inferidas (`estimated`) de explicitas (`exact`). UI appendea "(estimada)".
- Sin framework de migraciones; snapshots `.before-*` como marcadores de historia

## Alcance

- Modelo de datos (tabla, indices, views)
- Schema
- Invariantes

## Fuera de alcance

- UI de renderizado
- Generador del sitio
- Deploy
- Validacion automatica

## Preguntas pendientes

- TBD: `updated_at` esta declarado pero ningun script lo escribe — todos NULL. Decidir si se mantiene o se remueve.
- TBD: `notes` tiene datos en la DB pero `get_inventory` no lo SELECTa ni se renderiza. Decidir si se surfacea.
- TBD: las 3 views (current_inventory, purchase_history, skincare_spending) no se usan en el sitio. `skincare_spending` es analytics-ready sin UI. Decidir si se surfacea.
- TBD: `size_unit = 'unit'` esta permitido por schema pero no se usa en los datos actuales (solo ml/g).
- TBD: `product_type` enum se enforcea solo a nivel SQLite CHECK, no en la UI.
