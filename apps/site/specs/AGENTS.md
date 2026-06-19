# Convenciones de Specs

## Proposito

Specs vivas de Cosmetics: intencion, comportamiento, reglas de dominio y criterios verificables.

Fuente principal: `database/data/cosmetics.db` y `database/data/images/`.

El proyecto ya tiene codigo funcionando; las specs se reverse-engineeran desde el codigo existente, arrancan en `draft` para alinear codigo<->spec.

## Fronteras

- `specs/`: producto, dominio, comportamiento, reglas e invariantes verificables.
- `docs/adr/`: decisiones arquitectonicas aceptadas, contexto y consecuencias.
- `docs/architecture.md`: diseno tecnico derivado de specs.
- `database/README.md`: contrato de datos.
- `features/`: Gherkin ejecutable futuro, solo con hard spec aprobada.

El contrato de datos no es spec por defecto; solo si define comportamiento verificable o invariantes, no por describir el layout.

ADRs no son specs; documentan decisiones como markdown como DB o Python + GitHub Pages.

## Flujo minimo

1. `spec.md` como spec humana viva.
2. `hard-spec.md` solo cuando la spec este lista para requisitos verificables.
3. Gherkin en `features/` solo despues de aprobar la hard spec.
4. `tdd.md`, `traceability.md`, `review.md` o `mutation.md` bajo demanda, no como placeholders.

Cada avance de fase requiere aprobacion humana.

## Estados sugeridos

- `draft`: borrador humano abierto.
- `hard-spec-needed`: listo para endurecer.
- `hard-spec-approved`: requisitos verificables aprobados.
- `gherkin-needed`: falta Gherkin ejecutable.
- `ready-for-tdd`: Gherkin aprobado; se puede planear TDD.
- `implemented`: implementacion trazada contra la spec.
- `mutation-reviewed`: mutation testing revisado o justificado.

## Reglas de escritura

- Simple y concreto.
- Frontmatter YAML para metadatos: `title`, `status`, `description`.
- Separar hechos, inferencias y dudas.
- Nombrar la fuente sin copiar datos sensibles innecesariamente.
- Preferir ejemplos anonimizados.
- Marcar lo pendiente como `TBD` o pregunta, no como verdad.
- No convertir datos de cosmeticos ni de compras en hecho duro sin respaldo.
- No crear Gherkin, TDD, traceability, review o mutation vacios.
