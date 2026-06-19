# ADR 0002: Usar solo stdlib de Python

## Estado

Aceptada

## Contexto

El proyecto es un generador de sitio estático chico. Podría usar Streamlit, pandas, Jinja2 o un framework de frontend para templating y render.

Cada dependencia nueva suma superficie de supply chain, updates y conflicts. Para un proyecto de este tamaño eso pesa más que la comodidad del framework.

## Decisión

Usar únicamente el stdlib de Python. Cero dependencias en runtime. `dependencies = []` en `pyproject.toml`.

## Cómo funciona/interactúa

`build.py` usa `sqlite3`, `html`, `shutil`, `pathlib` y `dataclasses`, todo stdlib. El HTML, CSS y JS es vanilla e inline en un solo archivo.

Un test pinea que las strings `"streamlit"` y `"pandas"` no aparecen en `build.py`, protegiendo la decisión contra regresiones silenciosas.

## Tradeoffs

El stdlib gana para Cosmetics porque el proyecto es chico y no necesita abstracción de framework. Cero dependencias significa cero vulnerabilidades de supply chain, cero updates y cero conflicts.

Acepta que si el proyecto crece mucho, tareas como templating o paginación requerirán más código manual.

## Consecuencias

- No hay `package.json`, no hay `npm install`, no hay bundler.
- El build corre con `python3 apps/site/build.py`.
- Cualquier dependencia nueva requiere justificación fuerte.
- El test de no-regresión vigila que no entre un framework.
