# Cosmetics

Inventario personal de cosméticos generado como sitio estático desde SQLite.

La idea es simple: **SQLite es la fuente local de verdad** y `dist/` es el artefacto desplegable. Nada de servidores, nada de Streamlit, nada de runtime raro.

## Estructura

```txt
cosmetics/
├── build.py              # genera el sitio estático
├── schema.sql            # schema SQLite versionado
├── data/                 # datos locales: NO publicar sin revisar
│   ├── cosmetics.db
│   └── images/
├── dist/                 # salida generada para deploy
├── tests/
└── pyproject.toml
```

## Generar el sitio

```bash
python3 build.py
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
data/cosmetics.db
```

Las imágenes se referencian desde SQLite con paths relativos a `data/`, por ejemplo:

```txt
images/1.jpg
```

El generador abre SQLite en modo solo lectura (`mode=ro`) y copia al deploy solo las imágenes referenciadas por compras existentes.

## Deploy recomendado

Usá deploy estático. Para este proyecto, un backend sería overengineering.

### GitHub Pages

El deploy está automatizado con:

```bash
python3 publish_pages.py
```

Ese comando hace cuatro cosas:

1. exige que el working tree esté limpio;
2. genera `dist/` desde `data/cosmetics.db`;
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

Respaldá `data/` completo porque contiene la DB y las imágenes.
