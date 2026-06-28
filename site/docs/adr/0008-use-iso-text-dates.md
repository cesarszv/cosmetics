# ADR 0008: Usar fechas ISO como TEXT

## Estado

Aceptada

## Contexto

Las fechas (`purchase_date`, `ended_date`) podrían guardarse como tipo DATE de SQLite o timestamps unix. DATE tiene quirks de afinidad y los timestamps son ilegibles; para un inventario personal, la legibilidad importa.

## Decisión

Guardar fechas como `TEXT` en formato ISO `YYYY-MM-DD` con validación `GLOB '????-??-??'`.

## Cómo funciona/interactúa

Schema: `purchase_date TEXT NOT NULL CHECK(purchase_date GLOB '????-??-??')` y `ended_date TEXT CHECK(ended_date GLOB '????-??-??')`. El ordering funciona por comparación de strings. `ended_date_kind` distingue `exact` de `estimated`. El validador chequea `ended_date >= purchase_date` y el invariante paired-null entre `ended_date` y `ended_date_kind`.

## Tradeoffs

TEXT ISO gana para Cosmetics porque el orden lexicográfico coincide con el cronológico, es legible y no depende del tipo DATE de SQLite. Acepta validación de formato manual vía `GLOB`, no por tipo de columna.

## Consecuencias

- Las fechas se comparan como strings.
- Formato enforcea por `CHECK` más validador.
- `ended_date_kind` agrega metadata sobre la certeza de la fecha.
- El invariante paired-null evita estados incompletos.
