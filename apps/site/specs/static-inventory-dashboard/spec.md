---
title: Static Inventory Dashboard
status: draft
description: Generador de dashboard estatico a partir de la DB de compras de cosmeticos, sin backend ni framework de frontend
---

# Spec: Static Inventory Dashboard

## Intencion

Tomar las compras de cosmeticos guardadas en SQLite y publicarlas como un dashboard estatico navegable en GitHub Pages. Sin backend, sin framework de frontend, sin runtime dependencies. El generador lee la DB read-only, modela, renderiza HTML; el navegador solo busca y filtra.

## Contexto

- `apps/site/build.py` — generador del sitio estatico (353 lineas)
- `database/schema.sql` — esquema que consume (ver `cosmetic-purchase-model`)
- `database/data/cosmetics.db` — DB read-only
- `database/data/images/` — imagenes fuente
- `dist/` — output generado (gitignored)
- Relacionada con: `cosmetic-purchase-model`, `db-validation`, `site-deploy`

## Conceptos principales

### Generador

`build_site()` lee DB read-only, prepara rows, renderiza HTML, copia imagenes referenciadas, escribe `.nojekyll`. Pipeline procedural, sin clases (excepto `BuildResult` frozen dataclass como return type).

### Cards

Una card por fila de `cosmetic_purchases`. Orden: `purchase_date DESC, id DESC`. Brand se muestra uppercase sin label (no "Marca"). Size/type/price/date usan `<dl>`.

### Filtro client-side

Checkbox "Solo disponibles" (default ON) + busqueda libre sobre brand/name/category/type/size/dates. Busqueda en minusculas locale espanol. Atributo `data-search` precomputado en build time.

### Imagenes

`resolve_image` con path-traversal guard (`relative_to(root)` retorna None si escapa). Placeholder "Sin foto" para missing/broken. Dedup via `used_names` set con sufijos `-2`, `-3`. Renombradas a `purchase-<id>.<ext>` en dist. Solo se copian imagenes referenciadas por compras existentes.

### Precio

`format_price`: BOB cents a `Bs NN.NN`.

### Fechas

`format_finish_date`: appendea "(estimada)" cuando `ended_date_kind = estimated`.

### HTML escaping

`html.escape` en todos los campos user-controlled (brand, name, size, price, dates, search text, alt text, image URL).

## Principios

- DB read-only: `connect_read_only()` abre via `file:...?mode=ro` URI. Test pinea que INSERT raisea `OperationalError`.
- Zero runtime dependencies (test pinea que "streamlit" y "pandas" no aparecen en build.py)
- HTML escaping en todos los campos user-controlled
- Path traversal prevention en resolucion de imagenes
- Solo imagenes referenciadas se copian a `dist/`
- `.nojekyll` en cada build para que Pages sirva raw HTML/CSS/JS
- `loading="lazy"` en imagenes, `target="_blank" rel="noopener"` en links de imagen
- Sin paginacion — todas las rows en un HTML (fine a escala actual)

## Alcance

- `build.py` — generacion del sitio estatico, render, filtro, imagenes, formato

## Fuera de alcance

- Validacion de DB (ver `db-validation`)
- Deploy (ver `site-deploy`)
- Backend
- Framework de frontend

## Preguntas pendientes

- TBD: sin paginacion — todas las rows en un HTML. Repensar mas alla de ~cientos de rows.
- TBD: busqueda es substring client-side solo — sin fuzzy, sin field-specific, sin debouncing.
- TBD: HEIC originals committed alongside JPGs — conversion es manual, no automatizada.
- TBD: `dist/` esta gitignored pero actualmente presente en disco (stale artifact).
