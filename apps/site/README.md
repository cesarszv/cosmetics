# Cosmetics

Inventario personal de cosméticos generado como sitio estático desde SQLite.

La idea es simple: **SQLite es la fuente local de verdad** y `dist/` es el artefacto desplegable. Nada de servidores, nada de Streamlit, nada de runtime raro.

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

Salida esperada:

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

La base esperada es:

```txt
database/data/cosmetics.db
```

El modelo actual usa una tabla principal:

```txt
cosmetic_purchases
```

Cada fila representa una compra/unidad comprada. No existe una columna `available`: la disponibilidad se deriva de `ended_date`.

```txt
ended_date IS NULL     -> todavía lo tenés
ended_date IS NOT NULL -> se terminó o ya no lo tenés
```

Cuando una fecha fue inferida durante la carga inicial, queda marcada con:

```txt
ended_date_kind = estimated
```

Cuando vino explícitamente del export/manual:

```txt
ended_date_kind = exact
```

Las imágenes se referencian desde SQLite con paths relativos a `database/data/`, por ejemplo:

```txt
images/1.jpg
```

El generador abre SQLite en modo solo lectura (`mode=ro`) y copia al deploy solo las imágenes referenciadas por compras existentes.

## VSCode Tasks

Este repo versiona `.vscode/tasks.json` para automatizar lo repetitivo sin meter configuración personal del editor.

Tasks disponibles:

- `validate-db`: valida integridad, schema, fechas y fotos referenciadas.
- `test`: corre la suite de tests.
- `check`: corre `validate-db` y después `test`.
- `build-site`: genera `dist/` desde SQLite.
- `publish-pages`: publica `dist/` en GitHub Pages usando `publish_pages.py`.

## Deploy recomendado

Usá deploy estático. Para este proyecto, un backend sería overengineering.

### GitHub Pages

El deploy está automatizado con:

```bash
python3 apps/site/publish_pages.py
```

Ese comando hace cuatro cosas:

1. exige que el working tree esté limpio;
2. genera `dist/` desde `database/data/cosmetics.db`;
3. publica el contenido de `dist/` en la rama `gh-pages`;
4. intenta configurar GitHub Pages con `gh`.

Si la configuración automática falla, hacelo manualmente en GitHub:

```txt
Settings → Pages → Build and deployment
Source: Deploy from a branch
Branch: gh-pages
Folder: /root
```

Otras opciones razonables:

- Netlify: drag and drop de `dist/`.
- Cloudflare Pages: estático sólido.

## Advertencia sobre HEIC

Si las fotos están en `.heic`, algunos navegadores no las muestran bien. Para un deploy prolijo, convertí las imágenes fuente a `.jpg` o `.webp` antes de generar el sitio.

## Backup

Respaldá `database/data/` completo porque contiene la DB y las imágenes.
