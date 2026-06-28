Feature: DB Validation
  validate_db.py verifica integridad, schema, invariantes y datos
  antes de generar o publicar el sitio. Es el CI gate.

  @s1
  Scenario: DB valida pasa sin errores
    Given una DB con schema correcto y datos validos
    When validate_db corre
    Then imprime "DB valida" con counts de Compras, Actuales, Terminadas y Fechas estimadas

  @s2
  Scenario: DB inexistente raisea error
    Given que el archivo cosmetics.db no existe
    When validate_db corre
    Then raisea FileNotFoundError con mensaje "No existe la base esperada"

  @s3
  Scenario: Tabla faltante raisea error
    Given una DB sin tabla cosmetic_purchases
    When validate_db corre
    Then raisea RuntimeError con mensaje "Falta la tabla cosmetic_purchases"

  @s4
  Scenario: Columna available prohibida
    Given una DB con columna available en cosmetic_purchases
    When validate_db corre
    Then raisea RuntimeError con mensaje "No debe existir columna available"

  @s5
  Scenario: Paired-null inconsistente raisea error
    Given una DB con una fila donde ended_date es NULL pero ended_date_kind no-NULL
    When validate_db corre
    Then raisea RuntimeError con mensaje sobre fechas inconsistentes

  @s6
  Scenario: ended_date anterior a purchase_date raisea error
    Given una DB con una fila donde ended_date < purchase_date
    When validate_db corre
    Then raisea RuntimeError con mensaje sobre productos terminados antes de compra

  @s7
  Scenario: Precio negativo raisea error
    Given una DB con una fila donde price_bob_cents < 0
    When validate_db corre
    Then raisea RuntimeError con mensaje sobre precios negativos

  @s8
  Scenario: Size no-positivo raisea error
    Given una DB con una fila donde size_value <= 0
    When validate_db corre
    Then raisea RuntimeError con mensaje sobre tamanos invalidos

  @s9
  Scenario: Imagen referenciada faltante raisea error
    Given una DB con image_path apuntando a archivo inexistente
    When validate_db corre
    Then raisea RuntimeError con mensaje sobre imagenes faltantes

  @s10
  Scenario: Integrity check fallido raisea error
    Given una DB con corruption interna
    When validate_db corre
    Then raisea RuntimeError con mensaje "SQLite integrity_check fallo"

  @s11
  Scenario: Columnas faltantes raisea error
    Given una DB a la que le falta una columna de REQUIRED_COLUMNS
    When validate_db corre
    Then raisea RuntimeError con mensaje listando las columnas faltantes
