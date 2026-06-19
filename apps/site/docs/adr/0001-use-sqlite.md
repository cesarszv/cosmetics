# ADR 0001: Usar SQLite como fuente de verdad

## Estado

Aceptada

## Contexto

Cosmetics necesita un datastore local para inventario de compras de cosméticos. Es un proyecto personal, sin servidor, sin multi-usuario y sin concurrencia.

El dataset es chico y vive en una sola máquina. No hay necesidad de un motor externo ni de un servicio que operar.

## Decisión

Usar SQLite como fuente de verdad. El archivo `database/data/cosmetics.db` se commitea a git. `dist/` es un artefacto derivado, generado y gitignored.

## Cómo funciona/interactúa

El generador (`build.py`) abre la DB read-only vía `mode=ro` URI, nunca escribe. El validador (`validate_db.py`) chequea integridad antes de generar.

El schema vive en `database/schema.sql` versionado. No hay framework de migraciones; los snapshots `.before-*` sirven como marcadores de historia cuando el schema cambia a mano.

## Tradeoffs

SQLite gana para Cosmetics porque es un archivo, sin servidor, sin configuración, portable y commiteable.

Acepta que no sirve para concurrencia ni multi-usuario, pero el proyecto es single-user local.

## Consecuencias

- La DB es el source of truth; el sitio se regenera desde ella.
- Los cambios de schema son manuales, con snapshots como respaldo.
- No hay migraciones automáticas ni herramienta de diff de schema.
- El archivo `.db` se versiona; `dist/` no, porque se deriva.
