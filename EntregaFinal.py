import sqlite3

# Conexión a la base de datos SQLite
conn = sqlite3.connect("inventario.db")
cursor = conn.cursor()

# Crear la tabla si no existe
cursor.execute(
    """CREATE TABLE IF NOT EXISTS stock (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT NOT NULL,
        cantidad INTEGER NOT NULL,
        precio REAL NOT NULL,
        categoria TEXT NOT NULL
    )"""
)
conn.commit()

# Función para verificar si un producto existe en la base de datos
def elemento_existe(id_producto):
    cursor.execute("SELECT * FROM stock WHERE id = ?", (id_producto,))
    return cursor.fetchone() is not None

# Función para agregar un producto
def agregar_producto():
    print("\n*** AGREGAR PRODUCTO AL INVENTARIO ***")
    nombre = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese la descripción del producto: ")
    cantidad = int(input("Ingrese la cantidad del producto: "))
    precio = float(input("Ingrese el precio del producto: "))
    categoria = input("Ingrese la categoría del producto: ")

    cursor.execute(
        """INSERT INTO stock (nombre, descripcion, cantidad, precio, categoria)
        VALUES (?, ?, ?, ?, ?)""",
        (nombre, descripcion, cantidad, precio, categoria),
    )
    conn.commit()
    print(f"\nProducto '{nombre}' agregado con éxito.\n")

# Función para modificar un producto
def modificar_producto():
    print("\n*** MODIFICAR PRODUCTO ***")
    id_producto = int(input("Ingrese el ID del producto a modificar: "))
    if elemento_existe(id_producto):
        nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
        cursor.execute(
            "UPDATE stock SET cantidad = ? WHERE id = ?",
            (nueva_cantidad, id_producto),
        )
        conn.commit()
        print(f"\nProducto con ID {id_producto} actualizado con éxito.\n")
    else:
        print("\nProducto no encontrado.\n")

# Función para listar el inventario
def listar_inventario():
    print("\n*** INVENTARIO ACTUAL ***")
    cursor.execute("SELECT * FROM stock")
    productos = cursor.fetchall()
    if productos:
        print("ID | Nombre | Descripción | Cantidad | Precio | Categoría")
        print("-" * 60)
        for producto in productos:
            print(f"{producto[0]} | {producto[1]} | {producto[2]} | {producto[3]} | {producto[4]} | {producto[5]}")
    else:
        print("\nEl inventario está vacío.\n")

# Función para eliminar un producto
def eliminar_producto():
    print("\n*** ELIMINAR PRODUCTO ***")
    id_producto = int(input("Ingrese el ID del producto a eliminar: "))
    if elemento_existe(id_producto):
        cursor.execute("DELETE FROM stock WHERE id = ?", (id_producto,))
        conn.commit()
        print(f"\nProducto con ID {id_producto} eliminado con éxito.\n")
    else:
        print("\nProducto no encontrado.\n")

# Función para listar productos con bajo stock
def listar_bajo_stock():
    print("\n*** LISTAR PRODUCTOS BAJO STOCK ***")
    limite_stock = int(input("Ingrese el límite de stock: "))
    cursor.execute("SELECT * FROM stock WHERE cantidad <= ?", (limite_stock,))
    productos = cursor.fetchall()
    if productos:
        print("ID | Nombre | Descripción | Cantidad | Precio | Categoría")
        print("-" * 60)
        for producto in productos:
            print(f"{producto[0]} | {producto[1]} | {producto[2]} | {producto[3]} | {producto[4]} | {producto[5]}")
    else:
        print("\nNo hay productos con bajo stock.\n")

# Menú interactivo
def menu_interactivo():
    while True:
        print("\n*** MENÚ PRINCIPAL ***")
        print("1. Agregar producto")
        print("2. Modificar producto")
        print("3. Listar inventario")
        print("4. Eliminar producto")
        print("5. Listar productos bajo stock")
        print("6. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            modificar_producto()
        elif opcion == "3":
            listar_inventario()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            listar_bajo_stock()
        elif opcion == "6":
            print("\nSaliendo del programa...\n")
            break
        else:
            print("\nOpción inválida. Intente de nuevo.\n")

# Ejecutar el menú interactivo
menu_interactivo()

# Cerrar la conexión a la base de datos
conn.close()