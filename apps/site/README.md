# Cosmetics

Inventario personal de cosméticos. **SQLite es la fuente de verdad**, `dist/` es el artefacto desplegable. Sin servidores ni runtime.

## Estructura

```txt
cosmetics/
├── apps/                 # scripts de la app
│   └── site/
│       ├── build.py      # genera el sitio estático
│       ├── validate_db.py    # valida la base SQLite
│       └── publish_pages.py  # publica dist/ en GitHub Pages
├── database/             # datos locales: NO publicar sin revisar
│   ├── schema.sql        # schema SQLite versionado
│   └── data/
│       ├── cosmetics.db
│       └── images/
├── dist/                 # salida generada para deploy
├── tests/
└── pyproject.toml
```

## Generar el sitio

```bash
python3 apps/site/build.py
```

Salida:

```txt
dist/index.html
dist/images/
```

Abrí `dist/index.html` en el navegador o subí `dist/` a GitHub Pages, Netlify, Vercel o Cloudflare Pages.

## Tests

```bash
python3 -m pytest
```

## Datos

Base: `database/data/cosmetics.db`. Tabla principal: `cosmetic_purchases` (una fila = una compra). La disponibilidad se deriva de `ended_date`:

```txt
ended_date IS NULL     -> lo tenés
ended_date IS NOT NULL -> se terminó
```

`ended_date_kind` marca el origen de la fecha:

```txt
exact     -> vino del export/manual
estimated -> inferida durante la carga
```

Las imágenes se referencian con paths relativos a `database/data/` (ej: `images/1.jpg`). El generador abre SQLite read-only (`mode=ro`) y copia al deploy solo las imágenes referenciadas.

## VSCode Tasks

`.vscode/tasks.json` automatiza lo repetitivo sin configuración personal del editor.

- `validate-db`: valida integridad, schema, fechas y fotos referenciadas.
- `test`: corre la suite de tests.
- `check`: `validate-db` y después `test`.
- `build-site`: genera `dist/` desde SQLite.
- `publish-pages`: publica `dist/` en GitHub Pages.

## Deploy recomendado

Deploy estático; un backend sería overengineering.

### GitHub Pages

Automatizado con:

```bash
python3 apps/site/publish_pages.py
```

Hace: exige working tree limpio, genera `dist/` desde `database/data/cosmetics.db`, lo publica en `gh-pages`, e intenta configurar GitHub Pages con `gh`.

Si la configuración automática falla, manual en GitHub:

```txt
Settings → Pages → Build and deployment
Source: Deploy from a branch
Branch: gh-pages
Folder: /root
```

Otras opciones: Netlify (drag and drop de `dist/`), Cloudflare Pages.

## HEIC

Algunos navegadores no muestran `.heic`. Convertí las imágenes fuente a `.jpg` o `.webp` antes de generar.

## Backup

Respaldá `database/data/` completo (DB + imágenes).
