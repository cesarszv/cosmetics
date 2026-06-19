# ADR 0004: Usar tabla única denormalizada

## Estado

Aceptada

## Contexto

Los cosméticos tienen marca, producto, categoría y tipo. Podría haber tablas separadas con foreign keys. Para 10 rows single-user, la normalización agrega joins e integridad referencial sin valor concreto.

## Decisión

Usar una sola tabla `cosmetic_purchases` con `brand` y `product_name` como free-text. Sin foreign keys, sin tablas de referencia.

## Cómo funciona/interactúa

Una fila = una unidad comprada. `category` y `product_type` con enums vía `CHECK`; `brand` y `product_name` son free-text. Las views `current_inventory`, `purchase_history` y `skincare_spending` operan sobre la tabla base sin joins.

## Tradeoffs

Denormalización gana para Cosmetics porque el dataset es chico (10 rows) y single-user; no necesita integridad referencial. Acepta que no hay consistencia de nombres: "La Roche-Posay" y "Laroche Posay" serían dos marcas distintas.

## Consecuencias

- Sin joins; queries simples.
- `brand` y `product_name` free-text sin normalizar.
- Si se necesita consistencia de marcas, se normaliza después.
- Modelo intencionalmente simple y plano.
