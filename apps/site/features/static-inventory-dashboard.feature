Feature: Static Inventory Dashboard
  El generador build.py lee la DB read-only y produce un sitio estatico
  con cards, filtro client-side, imagenes y HTML escaping.

  @s1
  Scenario: Lee todos los productos con campos requeridos
    Given una DB con productos cargados
    When build_site genera el HTML
    Then cada producto aparece con nombre, tamano, precio y fecha de compra
    And la palabra "Marca" no aparece en el HTML

  @s2
  Scenario: Ordena compras por fecha descendente
    Given una DB con productos en distintas fechas
    When build_site genera el HTML
    Then las cards aparecen ordenadas por purchase_date DESC, id DESC

  @s3
  Scenario: Disponibilidad se deriva de ended_date
    Given una DB con un producto terminado y uno disponible
    When build_site prepara las filas
    Then el producto sin ended_date tiene available = True
    And el producto con ended_date tiene available = False

  @s4
  Scenario: Imagen faltante renderiza placeholder
    Given una DB con un producto sin image_path
    When build_site genera el HTML
    Then el HTML contiene "Sin foto"
    And cero imagenes son copiadas

  @s5
  Scenario: Imagen rota renderiza placeholder
    Given una DB con un producto con image_path inexistente
    When build_site genera el HTML
    Then el HTML contiene "Sin foto"
    And cero imagenes son copiadas

  @s6
  Scenario: Inventario vacio genera estado vacio
    Given una DB con cero productos
    When build_site genera el HTML
    Then el HTML contiene "No hay productos cargados"

  @s7
  Scenario: DB inexistente raisea error claro
    Given que el archivo cosmetics.db no existe
    When build_site intenta conectar
    Then raisea FileNotFoundError con mensaje "No existe la base de datos esperada"
    And no crea el archivo

  @s8
  Scenario: La conexion a DB es read-only
    Given una DB valida
    When se intenta hacer INSERT sobre la conexion read-only
    Then raisea OperationalError

  @s9
  Scenario: Formatea precio desde centavos
    Given un precio de 24600 centavos
    When se formatea con format_price
    Then el resultado es "Bs 246.00"

  @s10
  Scenario: HTML escapa campos user-controlled
    Given una DB con brand = "A&B" y name con tags script
    When build_site genera el HTML
    Then brand aparece como "A&amp;B"
    And los tags script aparecen escapados
    And no hay tags script crudos en el HTML

  @s11
  Scenario: Path traversal en imagen es bloqueado
    Given un image_path = "../outside.jpg"
    When resolve_image evalua el path
    Then retorna None
    And la imagen no se copia

  @s12
  Scenario: Solo imagenes referenciadas se copian
    Given una DB con un producto y una imagen no referenciada en data_dir
    When build_site genera el sitio
    Then dist/images/purchase-1.jpg existe
    And dist/images/unused.jpg no existe

  @s13
  Scenario: Filtro "Solo disponibles" activado por defecto
    Given el HTML generado por build_site
    When se inspecciona el checkbox de filtro
    Then el input tiene checked="checked" o checked

  @s14
  Scenario: Zero dependencias de runtime
    Given el source de build.py
    When se busca "streamlit" o "pandas"
    Then ninguna de las dos strings aparece

  @s15
  Scenario: Fecha estimada muestra sufijo
    Given un producto con ended_date_kind = "estimated"
    When format_finish_date formatea la fecha
    Then el resultado incluye "(estimada)"

  @s16
  Scenario: .nojekyll se escribe en cada build
    Given una DB valida
    When build_site genera el sitio
    Then dist/.nojekyll existe

  @s17
  Scenario: dist se wipea antes de cada build
    Given un dist/ pre-existente con archivos stale
    When build_site regenera el sitio
    Then los archivos stale no existen
    And solo index.html, .nojekyll e imagenes referenciadas existen
