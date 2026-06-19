# ADR 0001: Usar SQLite como fuente de verdad

## Estado

Aceptada

## Contexto

Inventario personal de cosméticos, single-user, sin concurrencia, dataset chico en una sola máquina. No requiere motor externo ni servicio que operar.

## Decisión

Usar SQLite como fuente de verdad. El archivo `database/data/cosmetics.db` se commitea a git. `dist/` es un artefacto derivado, generado y gitignored.

## Cómo funciona/interactúa

`build.py` abre la DB read-only (`mode=ro`). `validate_db.py` chequea integridad antes de generar. El schema vive en `database/schema.sql` versionado; no hay migraciones, los snapshots `.before-*` marcan historia cuando el schema cambia a mano.

## Tradeoffs

SQLite gana para Cosmetics porque es un archivo sin servidor, portable y commiteable. Acepta no servir para concurrencia ni multi-usuario, pero el proyecto es single-user local.

## Consecuencias

- DB es source of truth; el sitio se regenera desde ella.
- Cambios de schema manuales, con snapshots como respaldo.
- Sin migraciones automáticas ni diff de schema.
- `.db` se versiona; `dist/` no (derivado).
