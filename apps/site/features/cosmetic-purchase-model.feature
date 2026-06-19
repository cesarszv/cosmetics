Feature: Cosmetic Purchase Model
  La tabla unica cosmetic_purchases almacena compras de cosmeticos con invariantes:
  disponibilidad derivada, paired-null, integer cents, fechas ISO.

  @s1
  Scenario: La tabla tiene exactamente 15 columnas
    Given el schema de database/schema.sql
    When se inspecciona la tabla cosmetic_purchases
    Then tiene las columnas id, brand, product_name, category, product_type, size_value, size_unit, purchase_date, price_bob_cents, ended_date, ended_date_kind, image_path, notes, created_at, updated_at

  @s2
  Scenario: No existe columna available
    Given el schema de database/schema.sql
    When se inspecciona la tabla cosmetic_purchases
    Then no existe una columna llamada available

  @s3
  Scenario: Disponibilidad se deriva de ended_date
    Given una fila con ended_date IS NULL
    When se consulta la disponibilidad
    Then la fila es disponible

  @s4
  Scenario: Terminado se deriva de ended_date no-NULL
    Given una fila con ended_date no-NULL
    When se consulta la disponibilidad
    Then la fila no es disponible

  @s5
  Scenario: Paired-null de ended_date y ended_date_kind
    Given una fila con ended_date no-NULL y ended_date_kind NULL
    When se intenta insertar en la tabla
    Then el CHECK constraint rechaza la insercion

  @s6
  Scenario: ended_date debe ser mayor o igual a purchase_date
    Given una fila con ended_date anterior a purchase_date
    When se intenta insertar en la tabla
    Then el CHECK constraint rechaza la insercion

  @s7
  Scenario: Precio se guarda como integer cents
    Given una fila con price_bob_cents = 24600
    When se formatea el precio
    Then el resultado es "Bs 246.00"

  @s8
  Scenario: Fechas se guardan como TEXT ISO
    Given una fila con purchase_date = "2026-03-05"
    When se inspecciona el tipo de la columna
    Then es TEXT con CHECK GLOB '????-??-??'

  @s9
  Scenario: Category enum restringe valores
    Given una fila con category = "invalid"
    When se intenta insertar en la tabla
    Then el CHECK constraint rechaza la insercion

  @s10
  Scenario: Product_type enum restringe valores
    Given una fila con product_type = "invalid"
    When se intenta insertar en la tabla
    Then el CHECK constraint rechaza la insercion

  @s11
  Scenario: Size_value debe ser positivo si presente
    Given una fila con size_value = 0
    When se intenta insertar en la tabla
    Then el CHECK constraint rechaza la insercion

  @s12
  Scenario: La view current_inventory filtra disponibles
    Given filas con ended_date NULL y ended_date no-NULL
    When se consulta la view current_inventory
    Then retorna solo las filas con ended_date IS NULL

  @s13
  Scenario: La view purchase_history ordena por fecha descendente
    Given filas con distintas purchase_date
    When se consulta la view purchase_history
    Then retorna todas ordenadas por purchase_date DESC, id DESC
