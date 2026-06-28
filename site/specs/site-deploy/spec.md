---
title: Site Deploy
status: draft
description: Deploy reproducible del sitio estatico a GitHub Pages via git worktree y gh CLI
---

# Spec: Site Deploy

## Intencion

Publicar el sitio estatico a GitHub Pages de forma reproducible. Clean working tree requerido, build automatico, deploy via git worktree.

## Contexto

- `apps/site/publish_pages.py` — deployer (133 lineas)
- `apps/site/build.py` — se invoca antes del deploy (ver `static-inventory-dashboard`)
- `dist/` — output a publicar
- GitHub Pages — target (`gh-pages` branch, root folder)
- Relacionada con: `static-inventory-dashboard`, `db-validation`

## Conceptos principales

### Clean-tree guard

`require_clean_worktree`: aborta si hay cambios sin commitear.

### Build

Invoca `build.py` para regenerar `dist/`.

### Git worktree

Crea worktree en `gh-pages`, copia `dist/` al root, commitea, pushea.

### gh CLI

`gh repo view` para repo, `gh api repos/{repo}/pages` (GET/PATCH/POST) para Pages source. Fallback a instrucciones manuales si falla.

### .nojekyll

Bypass Jekyll en Pages.

## Principios

- Clean working tree requerido — sin deploys con cambios mezclados
- `dist/` generado, no se commitea a `main`
- Deploy manual via script o VSCode task — sin CI workflow file
- `gh-pages` orphan, solo contiene output de `dist/`

## Alcance

- `publish_pages.py` — deploy a GitHub Pages

## Fuera de alcance

- Generacion del sitio (ver `static-inventory-dashboard`)
- Validacion (ver `db-validation`)
- CI automatico

## Preguntas pendientes

- TBD: sin CI workflow file — deploy manual. Decidir si se agrega CI.
- TBD: `publish_pages.py` sin tests — side effects de git/gh por diseno.
- TBD: Netlify/Cloudflare Pages mencionados como alternativas en README pero no implementados.
