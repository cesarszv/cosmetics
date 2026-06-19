# Cosmetics Constitution

## Reglas

- La spec artesanal la escribe o edita una persona.
- La IA no inventa datos de cosmeticos ni de compras.
- No hay codigo nuevo sin spec aprobada; el existente se reverse-engineerea a specs.
- No hay implementacion nueva sin Gherkin aprobado.
- La implementacion futura sigue TDD.
- El mutation testing futuro mide calidad de tests, no reemplaza revision.
- SQLite es la fuente de verdad local; `dist/` es artefacto derivado (generado, no commiteado).
- Cero dependencias en runtime (verificado por test: ni streamlit, ni pandas).
- DB de solo lectura (`mode=ro` URI); el generador nunca muta la fuente.
- No existe columna `available`; la disponibilidad se deriva de `ended_date IS NULL` (el validador eleva error si la columna existe).
- Nulos emparejados: `ended_date` y `ended_date_kind` ambos NULL o ambos no-NULL.
- El dinero se guarda como centavos enteros (BOB), nunca como floats.
- Las fechas son TEXT ISO `YYYY-MM-DD` con validacion GLOB.
- Solo las imagenes referenciadas se copian a `dist/` (renombradas a `purchase-<id>.<ext>`).
- HTML escaping en todos los campos controlados por el usuario.
- Prevencion de path traversal en la resolucion de imagenes.
- La DB (`database/data/cosmetics.db`) y las imagenes se commitean a git.
- `database/data/` no se publica al sitio; `dist/` es lo que se publica.

## Fuentes protegidas

- DB de cosmeticos: `database/data/cosmetics.db`.
- Imagenes de compras: `database/data/images/`.
- Contrato de datos: `database/README.md`.
- Arquitectura: `docs/architecture.md`, `docs/adr/`.
