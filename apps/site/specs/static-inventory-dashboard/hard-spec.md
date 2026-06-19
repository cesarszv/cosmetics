# Hard Spec: Static Inventory Dashboard

Estado: hard-spec-needed

Fuente: `spec.md`

## Research base

- https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox — checkbox nativo con label clicable para "Solo disponibles".
- https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search — input de busqueda nativo con `type="search"`.
- https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/loading — `loading="lazy"` en imagenes fuera de viewport.
- https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a — `target="_blank" rel="noopener"` para links de imagen en nueva pestana.
- https://docs.python.org/3/library/html.html — `html.escape` para prevenir XSS en todos los campos user-controlled.
- https://docs.python.org/3/library/sqlite3.html#sqlite3.connect — URI `file:...?mode=ro` para conexion read-only.

## Decision de producto

100% estatico: un `index.html` con HTML/CSS/JS vanilla inline. El generador lee DB read-only, renderiza cards, copia solo imagenes referenciadas. El navegador filtra y busca client-side. Sin backend, sin framework, sin runtime dependencies.

## Requisitos verificables

- R1: `build_site` lee todas las filas de `cosmetic_purchases` y retorna una dict por fila.
- R2: Orden de filas `purchase_date DESC, id DESC` (tie-break por id descendente).
- R3: `available` se deriva de `ended_date IS NULL` (no se lee de columna).
- R4: `format_price` convierte integer cents a `Bs NN.NN` (ej: 24600 -> "Bs 246.00").
- R5: Brand uppercase sin label (no aparece "Marca" en el HTML).
- R6: Cada card tiene `<dl>` con 5 entradas: Tamano, Tipo, Precio, Compra, Terminado/no disponible.
- R7: `image_path = NULL` renderiza placeholder "Sin foto", no copia imagen.
- R8: `image_path` a archivo inexistente renderiza placeholder "Sin foto", no copia imagen.
- R9: Inventario vacio renderiza "No hay productos cargados".
- R10: DB inexistente raisea `FileNotFoundError` con "No existe la base de datos esperada", no crea archivo.
- R11: Conexion read-only via `file:...?mode=ro` URI; INSERT raisea `OperationalError`.
- R12: `build_site` escribe `dist/index.html` y `dist/.nojekyll`.
- R13: Solo imagenes referenciadas por compras existentes se copian a `dist/images/`.
- R14: Imagenes renombradas a `purchase-<id>.<ext>` en `dist/`.
- R15: Checkbox "Solo disponibles" tiene `checked` por defecto.
- R16: `build.py` no contiene "streamlit" ni "pandas".
- R17: `html.escape` en brand, name, size, product_type, price, purchase_date, finish_date, search text, image href/src/alt.
- R18: `resolve_image` retorna `None` para paths que escapan de data (path-traversal guard via `relative_to`).
- R19: `format_finish_date` appendea "(estimada)" si `ended_date_kind = 'estimated'`.
- R20: `build_site` wipea `dist/` (`shutil.rmtree`) antes de regenerar.
- R21: `data-search` se computa en build time como join lowercased de brand, name, category, product_type, size, purchase_date, finish_date.
- R22: `BuildResult` frozen dataclass con `output_file`, `rows`, `copied_images`.

## Reglas verificables

- V1: Conexion read-only (`mode=ro`); el generador nunca muta la DB fuente.
- V2: Cero runtime dependencies (solo stdlib: html, shutil, sqlite3, dataclasses, pathlib, typing).
- V3: `html.escape` en todos los campos user-controlled.
- V4: Path traversal prevention: `resolve_image` rechaza paths fuera de `database/data/`.
- V5: Solo imagenes referenciadas se copian a `dist/`.
- V6: `.nojekyll` se escribe en cada build.
- V7: `dist/` se wipea completo antes de cada build.
- V8: `loading="lazy"` en todas las imagenes.
- V9: Links de imagen usan `target="_blank" rel="noopener"`.
- V10: `category` es searchable pero no visible en la card.
- V11: JS de filtro usa `toLocaleLowerCase('es')`.

## UX y accesibilidad

- A1: `<html lang="es">` con `<meta charset="utf-8">` y viewport `width=device-width, initial-scale=1`.
- A2: Header con eyebrow "Inventario personal" y `<h1>` con el titulo.
- A3: Resumen `<p class="summary">` muestra disponibles y total con `<strong>`.
- A4: Toggle "Solo disponibles" usa `<label class="switch">` con checkbox nativo.
- A5: Busqueda usa `<input type="search">` con `autocomplete="off"`.
- A6: Grid usa `aria-live="polite"` para anunciar cambios de filtro.
- A7: Estado vacio usa `<p id="empty" hidden>` toggledo por JS.
- A8: Placeholder de imagen es texto, no `<img>` (no necesita alt).
- A9: CSS responsive con `@media (max-width: 680px)` que apila el hero.

## Casos limite

- C1: DB vacia (cero filas) genera grid vacio + mensaje visible, `rows=0`, `copied_images=0`.
- C2: DB inexistente raisea FileNotFoundError, no crea archivo.
- C3: `image_path` NULL o broken genera placeholder, no incrementa `copied`.
- C4: Path traversal `../x` se trata como sin imagen (placeholder).
- C5: Imagen sin extension usa suffix `.img` (ej: `purchase-1.img`).
- C6: Mismo `purchase_date` ordena por `id` descendente.
- C7: `dist/` pre-existente se wipea antes de rebuild.
- C8: `price_bob_cents = 0` renderiza `Bs 0.00`.
- C9: `ended_date_kind = 'estimated'` appendea "(estimada)"; `'exact'` no.
- C10: Imagenes no referenciadas se ignoran (no se copian).

## No requisitos

- N1: No paginacion (todas las filas en un HTML).
- N2: No filtro por categoria ni marca en UI (solo "Solo disponibles" + busqueda libre).
- N3: Busqueda no matchea price, `ended_date_kind`, ni image.
- N4: No optimizacion/resize/thumbnails (copy verbatim via `copy2`).
- N5: No tests de JS (JS inline no se ejercita con pytest).
- N6: No sitemap, robots.txt, favicon ni archivos extra a `index.html`, `.nojekyll` e imagenes.
- N7: No streamlit, no pandas, no dependencias de runtime.
- N8: No escritura a la DB (read-only).
- N9: `category` searchable pero no visible en la card.

## Preguntas pendientes

- TBD: sin paginacion — repensar mas alla de ~cientos de rows.
- TBD: busqueda substring client-side solo — sin fuzzy, sin field-specific.
- TBD: HEIC originals committed — conversion manual.
