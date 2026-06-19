# ADR 0002: Usar solo stdlib de Python

## Estado

Aceptada

## Contexto

Generador de sitio estático chico. Podría usar Streamlit, pandas, Jinja2 o un framework de frontend. Cada dependencia suma supply chain, updates y conflicts; a este tamaño pesa más que la comodidad del framework.

## Decisión

Usar únicamente el stdlib de Python. Cero dependencias en runtime; `dependencies = []` en `pyproject.toml`.

## Cómo funciona/interactúa

`build.py` usa `sqlite3`, `html`, `shutil`, `pathlib`, `dataclasses` (todo stdlib). HTML, CSS y JS vanilla inline en un archivo. Un test pinea que `"streamlit"` y `"pandas"` no aparecen en `build.py`, protegiendo contra regresiones.

## Tradeoffs

Stdlib gana para Cosmetics porque el proyecto es chico y no necesita abstracción de framework. Cero dependencias = cero supply chain, updates y conflicts. Acepta que si crece, templating o paginación requerirán más código manual.

## Consecuencias

- Sin `package.json`, `npm install` ni bundler.
- Build: `python3 apps/site/build.py`.
- Cualquier dependencia nueva requiere justificación fuerte.
- El test de no-regresión vigila que no entre un framework.
