# ADR 0005: Guardar dinero como centavos enteros

## Estado

Aceptada

## Contexto

Los precios están en Bolivianos (BOB). Podrían guardarse como float o string, pero los floats acumulan error de representación. Con dinero, no perder exactitud importa aunque el monto sea chico.

## Decisión

Guardar `price_bob_cents` como `INTEGER` (centavos). Nunca floats. `format_price` divide por 100 para mostrar `Bs NN.NN`.

## Cómo funciona/interactúa

Schema: `price_bob_cents INTEGER NOT NULL CHECK(price_bob_cents >= 0)`. `build.py` formatea con `format_price` (divide por 100, dos decimales). El validador chequea que ningún precio sea negativo.

## Tradeoffs

Centavos gana para Cosmetics porque evita errores de punto flotante: 24600 centavos siempre es `Bs 246.00`. Acepta que la UI debe formatear al mostrar, pero es una función de una línea.

## Consecuencias

- Sin floats en la DB.
- Cálculos de total, si se agregan, son exactos.
- Formato es responsabilidad de la UI, no del storage.
- El validador rechaza precios negativos.
