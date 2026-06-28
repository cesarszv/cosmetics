# ADR 0007: Publicar en GitHub Pages

## Estado

Aceptada

## Contexto

El sitio estático necesita un host. Alternativas: Netlify, Cloudflare Pages o un VPS con DNS y certificados. GitHub Pages ya está integrado al repo, sin costo ni DNS extra.

## Decisión

Publicar en GitHub Pages vía git worktree a la rama `gh-pages`.

## Cómo funciona/interactúa

`publish_pages.py` exige working tree limpio, invoca `build.py`, crea un worktree en `gh-pages`, copia `dist/` al root, commitea y pushea. Configura Pages con `gh` CLI y deja `.nojekyll` para bypassar Jekyll. Corre a mano o vía task de VSCode.

## Tradeoffs

GitHub Pages gana para Cosmetics porque es gratis, está integrado al repo y no requiere DNS ni CDN. Acepta deploy manual, sin CI workflow, y sitio público.

## Consecuencias

- Deploy manual vía script o task de VSCode.
- Sin CI automático por ahora.
- Sitio en `<user>.github.io/cosmetics`.
- Netlify o Cloudflare son alternativas no implementadas.
