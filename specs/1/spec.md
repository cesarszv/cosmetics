  <aside>
  📸

**Principio rector**: las fotos son el chiste. Cualquier decisión técnica que comprometa ver las imágenes de los productos está mal por definición.

  </aside>

## 1. Contexto

- Inventario personal de cosméticos, hoy en una base de datos de Notion, migrando a SQLite local.
- Modelo de datos ya definido: separación **producto** (catálogo) / **compra** (instancia), precio numérico en centavos, disponibilidad **derivada** de `finish_date`.

## 2. Objetivo del MVP

Un visor local, de un solo archivo de UI, que muestre todas las compras en una tabla tipo Notion **con thumbnails de las fotos**, lanzable con un solo comando.

**Dentro del alcance:**

- Tabla con foto, marca, nombre, tamaño, precio, fecha de compra y fecha de fin.
- Filtro "solo disponibles".
- Orden por fecha de compra descendente.
- Tolerancia a imágenes faltantes o rotas.

**Fuera del alcance (NO negociable para el MVP):**

- Alta, edición o borrado de productos (el visor es READ-ONLY).
- Autenticación, deploy, multi-usuario.
- Estadísticas, gráficos, historial de precios.
- Edición o procesamiento de imágenes.

## 3. Arquitectura

### Estructura del proyecto

```
cosmetics/
├── data/                  # datos del usuario — NO va a git
│   ├── cosmetics.db
│   └── images/            # nombradas por id de compra: 1.jpg, 2.jpg...
├── src/
│   └── visor.py           # UI Streamlit (única entrada del MVP)
├── tests/
│   └── test_visor.py
├── features/
│   └── visor.feature      # el Gherkin de la sección 5
├── schema.sql             # DDL versionado — SÍ va a git
├── pyproject.toml
└── README.md
```

### Stack

- **SQLite** como almacenamiento, archivo único `data/cosmetics.db`.
- **Streamlit + pandas** para la UI. Sin más dependencias.
- Imágenes en filesystem, la DB guarda solo el path **relativo** (`images/1.jpg`).
- Conexión **siempre** read-only: `file:...?mode=ro`.

### Schema (v1)

```sql
CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    brand TEXT NOT NULL,
    name TEXT NOT NULL,
    size TEXT,
    category TEXT
);

CREATE TABLE purchases (
    id INTEGER PRIMARY KEY,
    product_id INTEGER NOT NULL REFERENCES products(id),
    purchase_date DATE NOT NULL,
    price_bob INTEGER NOT NULL,   -- centavos de boliviano
    finish_date DATE,             -- NULL = disponible
    image_path TEXT               -- relativo a data/
);

CREATE VIEW available_products AS
SELECT * FROM purchases WHERE finish_date IS NULL;
```

### Separación lógica / presentación

Aun siendo un solo archivo, `visor.py` separa internamente:

- **Núcleo testeable** (funciones puras): `get_inventory()`, `format_price()`, `resolve_image()`. Sin imports de Streamlit. Esto es lo que se testea y se muta.
- **Capa de presentación**: el render de Streamlit. No se testea unitariamente ni se muta.

## 4. Hard Spec — Requisitos

### Funcionales

- **REQ-01** — El visor muestra todas las compras en una tabla con columnas: foto, marca, nombre, tamaño, precio, fecha de compra, fecha de fin.
- **REQ-02** — Cada fila muestra el thumbnail de su imagen, expandible al hacer click. Este es el requisito central del proyecto.
- **REQ-03** — Existe un toggle "solo disponibles" que filtra por `finish_date IS NULL`. La disponibilidad NUNCA se almacena como flag.
- **REQ-04** — Orden por defecto: `purchase_date` descendente.
- **REQ-05** — La conexión a la DB es de solo lectura. Ninguna ruta de código del visor puede escribir.
- **REQ-06** — Una imagen faltante (path NULL) o rota (archivo inexistente) muestra un placeholder. La aplicación jamás crashea por una imagen.
- **REQ-07** — Todos los paths se resuelven desde la raíz del proyecto vía `Path(__file__)`, nunca desde el directorio de ejecución.
- **REQ-08** — El precio se muestra formateado como `Bs 246.00` a partir del entero en centavos.
- **REQ-09** — Si la DB no existe, el visor muestra un error claro con la ruta esperada y NO crea un archivo nuevo.

### No funcionales

- Arranque con un solo comando: `streamlit run src/visor.py`.
- UI en un solo archivo mientras sea visor puro. Si se agrega escritura (post-MVP), se extrae `db.py` primero.
- Dependencias: stdlib + streamlit + pandas. Cada dependencia nueva requiere justificación.

### Decisiones tomadas (estilo Spec Partner)

1. **Imagen faltante → placeholder, no ocultar la fila.** Un inventario que esconde productos miente.
2. **Moneda fija en bolivianos.** No hay columna currency hasta que exista una compra real en otra moneda.
3. **Solo fecha, sin hora.** `purchase_date` y `finish_date` son DATE. Nadie registra a qué hora compró un protector solar.
4. **El filtro "disponibles" arranca activado.** El caso de uso dominante es "¿qué tengo ahora?".

## 5. Contrato ejecutable (Gherkin)

```gherkin
# language: es
Característica: Visor de inventario de cosméticos
  Como dueño del inventario
  Quiero ver mis productos en una tabla con sus fotos
  Para saber qué tengo, qué se terminó y cuánto costó

  Antecedentes:
    Dado que existe "data/cosmetics.db" con el schema v1

  # S1 — camino feliz
  Escenario: Ver todos los productos con su foto
    Dado un inventario con 3 compras con image_path válido
    Cuando abro el visor sin filtros
    Entonces veo una tabla con 3 filas
    Y cada fila muestra el thumbnail de su imagen
    Y cada fila muestra marca, nombre, tamaño, precio y fecha de compra

  # S2 — orden
  Escenario: Las compras se ordenan por fecha descendente
    Dado compras con fechas 2026-01-10, 2026-03-05 y 2026-02-01
    Cuando abro el visor
    Entonces la primera fila es la compra del 2026-03-05

  # S3 — disponibilidad derivada
  Escenario: Filtrar solo productos disponibles
    Dado 2 compras con finish_date NULL y 1 con finish_date 2026-04-30
    Cuando activo el filtro "solo disponibles"
    Entonces veo exactamente 2 filas

  # S4 — imagen no registrada
  Escenario: Compra sin imagen
    Dado una compra con image_path NULL
    Cuando abro el visor
    Entonces esa fila muestra un placeholder
    Y la aplicación no lanza ningún error

  # S5 — imagen rota
  Escenario: image_path apunta a un archivo inexistente
    Dado una compra con image_path "images/999.jpg" inexistente en disco
    Cuando abro el visor
    Entonces esa fila muestra un placeholder
    Y la aplicación no lanza ningún error

  # S6 — inventario vacío
  Escenario: Base de datos sin compras
    Dado una base de datos vacía con schema v1
    Cuando abro el visor
    Entonces veo el mensaje "No hay productos cargados"

  # S7 — DB ausente
  Escenario: La base de datos no existe
    Dado que no existe el archivo "data/cosmetics.db"
    Cuando abro el visor
    Entonces veo un error claro con la ruta esperada
    Y no se crea ningún archivo .db nuevo

  # S8 — solo lectura
  Escenario: El visor no puede escribir
    Dado el visor conectado a la base de datos
    Cuando se intenta ejecutar un INSERT, UPDATE o DELETE
    Entonces la operación falla por conexión de solo lectura

  # S9 — formato de precio
  Escenario: El precio se muestra formateado
    Dado una compra con price_bob igual a 24600
    Cuando abro el visor
    Entonces esa fila muestra el precio "Bs 246.00"
```

## 6. Flujo de desarrollo (el arnés)

1. **Spec** — este documento. Revisión humana obligatoria antes de tocar código.
2. **Gherkin** — sección 5, se copia a `features/visor.feature`. Cada escenario tiene ID estable (S1–S9).
3. **TDD** — con pytest, las tres leyes: test en rojo → código mínimo → refactor. Un ciclo por escenario, registrado en el log de progreso.
4. **Juez** — checklist antes de cerrar:


    - [ ] Cada escenario S1–S9 tiene al menos un test que lo referencia por ID.
    - [ ] Ningún test toca la DB real de `data/` (usar DB temporal en memoria o tmp_path).
    - [ ] El núcleo testeable no importa Streamlit.
    - [ ] Hubo ciclos rojo → verde registrados, no tests escritos después del código.

5. **Mutation testing** — con `mutmut` (no reinventar el script de mutaciones, ya existe la herramienta madura para Python) sobre el núcleo testeable de `src/`. Todo mutante superviviente dentro del alcance del MVP exige un test nuevo: handoff de vuelta al paso 3.

## 7. Definition of Done

- [ ] `streamlit run src/visor.py` levanta la tabla con fotos visibles.
- [ ] Los 9 escenarios Gherkin tienen tests en verde.
- [ ] `mutmut` sin supervivientes dentro del alcance.
- [ ] La conexión es read-only verificada por test (S8).
- [ ] `schema.sql` y `features/visor.feature` versionados en git; `data/` en `.gitignore`.
- [ ] README con: cómo correr el visor, cómo correr los tests, cómo hacer backup (zip de `data/`).
