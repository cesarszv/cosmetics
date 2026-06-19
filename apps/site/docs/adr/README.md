# ADRs de Cosmetics

Indice de decisiones de arquitectura para entender el rumbo tecnico sin releer cada ADR.

| Nro. | Decision | Estado | Resumen | Link |
| --- | --- | --- | --- | --- |
| 0001 | Usar SQLite como fuente de verdad | Aceptada | DB local commiteada a git; el sitio se regenera desde ella. | [0001-use-sqlite.md](0001-use-sqlite.md) |
| 0002 | Usar solo stdlib de Python | Aceptada | Cero dependencias en runtime; build con sqlite3, html, pathlib. | [0002-use-python-stdlib-only.md](0002-use-python-stdlib-only.md) |
| 0003 | Derivar disponibilidad de ended_date | Aceptada | No hay columna available; se computa de ended_date IS NULL. | [0003-derive-availability-from-ended-date.md](0003-derive-availability-from-ended-date.md) |
| 0004 | Usar tabla unica denormalizada | Aceptada | Una sola tabla cosmetic_purchases, sin foreign keys ni joins. | [0004-use-single-denormalized-table.md](0004-use-single-denormalized-table.md) |
| 0005 | Guardar dinero como centavos enteros | Aceptada | price_bob_cents INTEGER; formato Bs NN.NN solo en la UI. | [0005-store-money-as-integer-cents.md](0005-store-money-as-integer-cents.md) |
| 0006 | Generar sitio estatico sin backend | Aceptada | HTML/CSS/JS vanilla inline; filtro client-side sobre datos pre-renderizados. | [0006-generate-static-site.md](0006-generate-static-site.md) |
| 0007 | Publicar en GitHub Pages | Aceptada | Deploy manual via worktree a gh-pages con .nojekyll. | [0007-deploy-to-github-pages.md](0007-deploy-to-github-pages.md) |
| 0008 | Usar fechas ISO como TEXT | Aceptada | YYYY-MM-DD con GLOB; ordering lexicografico igual al cronologico. | [0008-use-iso-text-dates.md](0008-use-iso-text-dates.md) |

## Flujo actual

Cosmetics es un generador de sitio estatico single-user. Fuente de verdad: SQLite (`database/data/cosmetics.db`) commiteada a git. Schema en `database/schema.sql`; tabla base `cosmetic_purchases` denormalizada, enums por CHECK, dinero en centavos enteros.

`build.py` abre la DB read-only con stdlib y renderiza un `index.html` vanilla inline. `validate_db.py` enforcea invariantes antes de generar (no columna `available`, fechas ISO, precios no negativos, paired-null). Deploy manual: `publish_pages.py` copia `dist/` a `gh-pages` via worktree y configura GitHub Pages.
