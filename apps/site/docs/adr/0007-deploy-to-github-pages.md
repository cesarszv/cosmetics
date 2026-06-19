# ADR 0007: Publicar en GitHub Pages

## Estado

Aceptada

## Contexto

El sitio estático necesita un host. Podría usar Netlify, Cloudflare Pages o un VPS con su DNS y certificados.

GitHub Pages ya está integrado al repo donde vive el proyecto, sin costo ni configuración extra de DNS.

## Decisión

Publicar en GitHub Pages vía git worktree a la rama `gh-pages`.

## Cómo funciona/interactúa

`publish_pages.py` exige working tree limpio, invoca `build.py`, crea un worktree en `gh-pages`, copia `dist/` al root, commitea y pushea. Configura Pages con la `gh` CLI y deja un `.nojekyll` para bypassar Jekyll.

El script corre a mano o por una task de VSCode.

## Tradeoffs

GitHub Pages gana para Cosmetics porque es gratis, está integrado al repo y no requiere DNS ni CDN.

Acepta que el deploy es manual, sin CI workflow, y que el sitio es público.

## Consecuencias

- Deploy manual vía script o task de VSCode.
- Sin CI automático por ahora.
- El sitio vive en `<user>.github.io/cosmetics`.
- Netlify o Cloudflare son alternativas no implementadas.
