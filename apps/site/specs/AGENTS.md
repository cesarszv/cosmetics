# Convenciones de Specs

## Proposito

Esta carpeta contiene las specs vivas de Cosmetics. Una spec describe intencion, comportamiento, reglas de dominio y criterios verificables.

Fuente principal: `database/data/cosmetics.db` y `database/data/images/`.

Este proyecto ya tiene codigo funcionando. Las specs aqui se reverse-engineeran desde el codigo existente; el estado arranca en `draft` con la intencion de alinear codigo↔spec de aqui en adelante.

## Fronteras

- `specs/`: producto, dominio, comportamiento, reglas e invariantes verificables.
- `docs/adr/`: decisiones arquitectonicas aceptadas, contexto y consecuencias.
- `docs/architecture.md`: diseno tecnico derivado de specs.
- `database/README.md`: contrato de datos.
- `features/`: Gherkin ejecutable futuro, solo cuando haya hard spec aprobada.

El contrato de datos no es una spec por defecto. Una spec de datos solo existe si define comportamiento verificable o invariantes, no por describir el layout.

ADRs no son specs. Documentan decisiones como markdown como DB o Python + GitHub Pages.

## Flujo minimo

1. Mantener `spec.md` como spec humana viva.
2. Crear `hard-spec.md` solo cuando la spec este lista para requisitos verificables.
3. Crear Gherkin en `features/` solo despues de aprobar la hard spec.
4. Crear `tdd.md`, `traceability.md`, `review.md` o `mutation.md` bajo demanda, no como placeholders.

Cada avance de fase requiere aprobacion humana.

## Estados sugeridos

- `draft`: borrador humano abierto.
- `hard-spec-needed`: la spec esta lista para endurecer.
- `hard-spec-approved`: los requisitos verificables fueron aprobados.
- `gherkin-needed`: falta Gherkin ejecutable.
- `ready-for-tdd`: Gherkin aprobado; se puede planear TDD.
- `implemented`: hay implementacion trazada contra la spec.
- `mutation-reviewed`: mutation testing revisado o justificado.

## Reglas de escritura

- Escribir simple y concreto.
- Usar frontmatter YAML para metadatos de specs: `title`, `status`, `description`.
- Separar hechos, inferencias y dudas.
- Nombrar la fuente sin copiar datos sensibles innecesariamente.
- Preferir ejemplos anonimizados.
- Marcar lo pendiente como `TBD` o pregunta, no como verdad.
- No convertir datos de cosmeticos ni de compras en hecho duro sin respaldo.
- No crear Gherkin, TDD, traceability, review o mutation vacios para todo.
