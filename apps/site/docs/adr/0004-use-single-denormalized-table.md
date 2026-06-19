# ADR 0004: Usar tabla única denormalizada

## Estado

Aceptada

## Contexto

Los cosméticos tienen marca, producto, categoría y tipo. Podría haber tablas separadas para brands, products y categories con foreign keys.

Para 10 rows single-user, la normalización agrega joins e integridad referencial que no aportan valor concreto.

## Decisión

Usar una sola tabla `cosmetic_purchases` con `brand` y `product_name` como free-text. Sin foreign keys, sin tablas de referencia.

## Cómo funciona/interactúa

Una fila equivale a una unidad comprada. `category` y `product_type` tienen enums vía `CHECK` constraints. `brand` y `product_name` son free-text.

Las views `current_inventory`, `purchase_history` y `skincare_spending` operan sobre la tabla base, sin joins.

## Tradeoffs

La denormalización gana para Cosmetics porque el dataset es chico (10 rows) y single-user. No hay necesidad de integridad referencial.

Acepta que no hay consistencia de nombres de marca o producto: "La Roche-Posay" y "Laroche Posay" serían dos marcas distintas.

## Consecuencias

- No hay joins; las queries son simples.
- `brand` y `product_name` son free-text sin normalizar.
- Si se necesita consistencia de marcas, se normaliza después.
- El modelo es intencionalmente simple y plano.
