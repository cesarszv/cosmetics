---
title: Site Deploy
status: draft
description: Deploy reproducible del sitio estatico a GitHub Pages via git worktree y gh CLI
---

# Spec: Site Deploy

## Intencion

Publicar el sitio estatico generado a GitHub Pages de forma reproducible. Clean working tree requerido, build automatico, deploy via git worktree.

## Contexto

- `apps/site/publish_pages.py` — deployer (133 lineas)
- `apps/site/build.py` — se invoca antes del deploy (ver `static-inventory-dashboard`)
- `dist/` — output a publicar
- GitHub Pages — target (`gh-pages` branch, root folder)
- Relacionada con: `static-inventory-dashboard`, `db-validation`

## Conceptos principales

### Clean-tree guard

`require_clean_worktree`: si hay cambios sin commitear, aborta.

### Build

Invoca `build.py` para regenerar `dist/`.

### Git worktree

Crea worktree en `gh-pages` branch, copia `dist/` al root, commitea, pushea.

### gh CLI

`gh repo view` para obtener repo, `gh api repos/{repo}/pages` (GET/PATCH/POST) para configurar Pages source. Fallback a instrucciones manuales si falla.

### .nojekyll

Bypass Jekyll en Pages.

## Principios

- Clean working tree requerido — sin deploys accidentales con cambios mezclados
- `dist/` es generado, no se commitea a `main`
- Deploy manual via script o VSCode task — sin CI workflow file
- `gh-pages` branch es orphan, solo contiene el output de `dist/`

## Alcance

- `publish_pages.py` — deploy a GitHub Pages

## Fuera de alcance

- Generacion del sitio (ver `static-inventory-dashboard`)
- Validacion (ver `db-validation`)
- CI automatico

## Preguntas pendientes

- TBD: sin CI workflow file (`.github/workflows/` ausente) — deploy es manual. Decidir si se agrega CI.
- TBD: `publish_pages.py` no tiene tests — side effects de git/gh por diseno.
- TBD: Netlify/Cloudflare Pages mencionados como alternativas en README pero no implementados.
