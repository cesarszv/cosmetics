# Hard Spec: Site Deploy

Estado: hard-spec-needed

Fuente: `spec.md`

## Requisitos verificables

- R1: `main()` ejecuta la secuencia: clean-tree guard -> repo name -> build -> deploy worktree -> configure Pages.
- R2: `build_site` corre `[sys.executable, "apps/site/build.py"]` como subprocess.
- R3: Si build falla, el deploy aborta (CalledProcessError con check=True).
- R4: El commit message del deploy es "deploy: publish static site".
- R5: Si no hay cambios para publicar, imprime "No hay cambios para publicar en gh-pages." y no commitea ni pushea.
- R6: `configure_pages` setea source a `{"branch": "gh-pages", "path": "/"}`.
- R7: Si Pages API falla, imprime instrucciones manuales y no raisea.

## Reglas verificables

- V1: `require_clean_worktree` corre `git status --porcelain`; si hay output non-empty, aborta con SystemExit antes de build.
- V2: `repo_name_with_owner` usa `gh repo view --json nameWithOwner`.
- V3: Si branch local `gh-pages` existe, usa `git worktree add {target} gh-pages`.
- V4: Si solo branch remoto existe, usa `git worktree add -b gh-pages {target} origin/gh-pages`.
- V5: Si no existe branch local ni remoto, crea orphan via `git checkout --orphan gh-pages`.
- V6: `clean_directory` remueve todo excepto `.git` antes de copiar `dist/`.
- V7: `copy_dist` copia todo el contenido de `dist/` al root del worktree.
- V8: `publish_worktree` hace `git add --all`, commitea y pushea solo si hay cambios.
- V9: `configure_pages` usa PATCH si Pages ya existe, POST si no.
- V10: Worktree cleanup: `git worktree remove --force` al final dentro de TemporaryDirectory.
- V11: `configure_pages` corre incondicionalmente, incluso cuando no hay cambios.

## Casos limite

- C1: No cambios para publicar -> no commit, no push, pero configure_pages corre.
- C2: Primer deploy (sin branch local ni remoto) -> orphan branch creado, directorio limpiado, dist copiado.
- C3: Pages API falla -> non-fatal, imprime instrucciones manuales.
- C4: Build falla -> CalledProcessError antes de cualquier mutacion de git.
- C5: Working tree sucio -> SystemExit antes de `gh repo view` y antes de build.
- C6: `.nojekyll` es producido por build.py y llevado al worktree por copy_dist.

## No requisitos

- N1: No tests — por diseno (side effects de git/gh).
- N2: No `--dry-run` / modo preview.
- N3: No rollback on partial failure.
- N4: Commit message fijo "deploy: publish static site" (sin co-author, sin body).
- N5: No force push.
- N6: Deployer no valida la DB — confia en que build.py exit 0.
- N7: No verifica que index.html sea non-empty.
- N8: Pages source siempre `gh-pages` / `/` (root); no subpath, no custom domain.

## Preguntas pendientes

- TBD: sin CI workflow file — deploy manual. Decidir si se agrega CI.
- TBD: `publish_pages.py` sin tests — side effects de git/gh por diseno.
- TBD: Netlify/Cloudflare Pages mencionados pero no implementados.
