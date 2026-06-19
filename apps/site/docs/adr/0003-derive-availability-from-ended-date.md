# ADR 0003: Derivar disponibilidad de ended_date

## Estado

Aceptada

## Contexto

Un cosmético está "disponible" (en uso) o "terminado". Una columna `available` booleana duplicaría info que ya vive en `ended_date` y podría desincronizarse.

## Decisión

No tener columna `available`. La disponibilidad se deriva de `ended_date IS NULL`. El validador RAISEa si encuentra una columna `available`.

## Cómo funciona/interactúa

`prepare_rows` en `build.py` computa `available = finish_date is None`; el filtro client-side usa `data-available`. El schema no define la columna y el validador enforcea su ausencia. `test_s3` pinea esta derivación.

## Tradeoffs

Derivar gana para Cosmetics porque evita un estado redundante que puede contradecir a `ended_date` (una `available` podría decir "disponible" con `ended_date` cargado). Acepta que cada query computa la derivación, pero con 10 rows es trivial.

## Consecuencias

- Sin columna `available` en el schema.
- El validador rechaza cualquier DB que la tenga.
- Disponibilidad siempre consistente con `ended_date`.
- Invariante central del modelo de inventario.
