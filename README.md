# Cosmetics

Visor local read-only para el inventario personal de cosméticos.

## Correr el visor

```bash
streamlit run src/visor.py
```

La base esperada es `data/cosmetics.db`. El visor abre SQLite en modo solo lectura (`mode=ro`), así que no crea ni modifica la DB.

## Correr tests

```bash
python3 -m pytest
```

## Mutation testing

```bash
mutmut run
```

## Backup

Respaldar `data/` completo, porque contiene `cosmetics.db` y `images/`:

```bash
zip -r cosmetics-data-backup.zip data/
```

## Datos importados

Este workspace fue construido desde el export de Notion en `ExportBlock-7c65a935-7241-411b-aa9c-05481ff3f6be-Part-1`.

Las imágenes HEIC se guardan sin conversión en `data/images/`. El visor las incrusta con MIME `image/heic`; se verán si el navegador soporta HEIC y mostrarán placeholder si faltan o están rotas.
