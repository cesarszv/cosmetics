# language: es
Característica: Visor de inventario de cosméticos
  Como dueño del inventario
  Quiero ver mis productos en una tabla con sus fotos
  Para saber qué tengo, qué se terminó y cuánto costó

  Antecedentes:
    Dado que existe "data/cosmetics.db" con el schema v1

  # S1 - camino feliz
  Escenario: Ver todos los productos con su foto
    Dado un inventario con 3 compras con image_path válido
    Cuando abro el visor sin filtros
    Entonces veo una tabla con 3 filas
    Y cada fila muestra el thumbnail de su imagen
    Y cada fila muestra marca, nombre, tamaño, precio y fecha de compra

  # S2 - orden
  Escenario: Las compras se ordenan por fecha descendente
    Dado compras con fechas 2026-01-10, 2026-03-05 y 2026-02-01
    Cuando abro el visor
    Entonces la primera fila es la compra del 2026-03-05

  # S3 - disponibilidad derivada
  Escenario: Filtrar solo productos disponibles
    Dado 2 compras con finish_date NULL y 1 con finish_date 2026-04-30
    Cuando activo el filtro "solo disponibles"
    Entonces veo exactamente 2 filas

  # S4 - imagen no registrada
  Escenario: Compra sin imagen
    Dado una compra con image_path NULL
    Cuando abro el visor
    Entonces esa fila muestra un placeholder
    Y la aplicación no lanza ningún error

  # S5 - imagen rota
  Escenario: image_path apunta a un archivo inexistente
    Dado una compra con image_path "images/999.jpg" inexistente en disco
    Cuando abro el visor
    Entonces esa fila muestra un placeholder
    Y la aplicación no lanza ningún error

  # S6 - inventario vacío
  Escenario: Base de datos sin compras
    Dado una base de datos vacía con schema v1
    Cuando abro el visor
    Entonces veo el mensaje "No hay productos cargados"

  # S7 - DB ausente
  Escenario: La base de datos no existe
    Dado que no existe el archivo "data/cosmetics.db"
    Cuando abro el visor
    Entonces veo un error claro con la ruta esperada
    Y no se crea ningún archivo .db nuevo

  # S8 - solo lectura
  Escenario: El visor no puede escribir
    Dado el visor conectado a la base de datos
    Cuando se intenta ejecutar un INSERT, UPDATE o DELETE
    Entonces la operación falla por conexión de solo lectura

  # S9 - formato de precio
  Escenario: El precio se muestra formateado
    Dado una compra con price_bob igual a 24600
    Cuando abro el visor
    Entonces esa fila muestra el precio "Bs 246.00"
