# ADR 0006: Generar sitio estático sin backend

## Estado

Aceptada

## Contexto

El inventario podría servirse desde un backend, un SPA o un framework como Streamlit. Cada opción suma un runtime que mantener.

Para mostrar un catálogo chico que cambia poco, un sitio estático es suficiente y más simple de publicar.

## Decisión

Generar un sitio estático (HTML, CSS y JS vanilla) desde la DB. Sin backend, sin framework de frontend, sin runtime.

## Cómo funciona/interactúa

`build.py` lee la DB read-only y renderiza un `index.html` con todo inline. El navegador solo busca y filtra client-side sobre datos pre-renderizados.

`dist/` es el output. Se publica a GitHub Pages (ADR 0007).

## Tradeoffs

Estático gana para Cosmetics porque no necesita servidor, no tiene costo de hosting y es instantáneo. El sitio es un solo archivo HTML.

Acepta que no hay interactividad server-side: el filtro es client-side sobre datos pre-renderizados.

## Consecuencias

- El sitio es un artefacto derivado, no la fuente.
- Cualquier cambio requiere regenerar.
- Sin paginación: todas las rows viven en un HTML.
- Sin backend que mantener ni actualizar.
