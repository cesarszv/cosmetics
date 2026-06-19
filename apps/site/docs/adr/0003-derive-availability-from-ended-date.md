# ADR 0003: Derivar disponibilidad de ended_date

## Estado

Aceptada

## Contexto

Un cosmético puede estar "disponible" (en uso) o "terminado". Podría existir una columna `available` booleana en la tabla.

Esa columna duplicaría información que ya vive en `ended_date`, abriendo la puerta a que los dos estados se desincronicen.

## Decisión

No tener columna `available`. La disponibilidad se deriva de `ended_date IS NULL`. El validador RAISEa si encuentra una columna `available`.

## Cómo funciona/interactúa

`prepare_rows` en `build.py` computa `available = finish_date is None`. El filtro client-side usa el atributo `data-available` derivado de ese cálculo.

El schema no define la columna. El validador enforcea su ausencia. Un test (`test_s3`) pinea esta derivación para que no se rompa sin avisar.

## Tradeoffs

Derivar gana para Cosmetics porque evita un estado redundante que puede contradecir a `ended_date`. Una columna `available` podría decir "disponible" con `ended_date` cargado.

Acepta que cada query debe computar la derivación, pero con 10 rows es trivial.

## Consecuencias

- No hay columna `available` en el schema.
- El validador rechaza cualquier DB que la tenga.
- La disponibilidad siempre es consistente con `ended_date`.
- Es el invariante central del modelo de inventario.
