# Sistema de Gestión de Inventario

## Descripción
Este programa permite gestionar un inventario de productos almacenados en una base de datos SQLite. Incluye funciones para agregar, modificar, listar, eliminar productos y consultar productos con bajo stock.

## Requisitos
- Python 3.6 o superior
- Módulo SQLite3 (incluido por defecto en Python)

## Cómo usar el sistema
1. **Ejecutar el programa**:
   - Asegúrese de tener el archivo `inventario.db` en el mismo directorio que este script. Si no existe, se creará automáticamente al iniciar el programa.

2. **Opciones disponibles en el menú**:

   ### 1. Agregar producto
   - Permite agregar un nuevo producto al inventario.
   - Solicita ingresar:
     - Nombre
     - Descripción
     - Cantidad
     - Precio
     - Categoría

   ### 2. Modificar producto
   - Permite actualizar la cantidad de un producto existente.
   - Solicita el ID del producto a modificar.

   ### 3. Listar inventario
   - Muestra todos los productos en el inventario.
   - Formato:
     - ID | Nombre | Descripción | Cantidad | Precio | Categoría

   ### 4. Eliminar producto
   - Permite eliminar un producto del inventario.
   - Solicita el ID del producto a eliminar.

   ### 5. Listar productos bajo stock
   - Muestra los productos cuya cantidad sea menor o igual a un límite especificado por el usuario.
   - Formato:
     - ID | Nombre | Descripción | Cantidad | Precio | Categoría

   ### 6. Salir
   - Finaliza el programa y cierra la conexión con la base de datos.

## Estructura de la base de datos
La base de datos `inventario.db` contiene una tabla llamada `stock` con la siguiente estructura:

| Campo       | Tipo    | Descripción                                    |
|-------------|---------|------------------------------------------------|
| id          | INTEGER | Identificador único del producto              |
| nombre      | TEXT    | Nombre del producto                           |
| descripcion | TEXT    | Descripción del producto                      |
| cantidad    | INTEGER | Cantidad disponible en el inventario          |
| precio      | REAL    | Precio del producto                           |
| categoria   | TEXT    | Categoría del producto                        |

## Ejemplo de uso
### Agregar producto:
```
Ingrese el nombre del producto: Manzanas
Ingrese la descripción del producto: Fruta fresca
Ingrese la cantidad del producto: 50
Ingrese el precio del producto: 0.5
Ingrese la categoría del producto: Alimentos

Producto 'Manzanas' agregado con éxito.
```

### Listar inventario:
```
*** INVENTARIO ACTUAL ***
ID | Nombre       | Descripción   | Cantidad | Precio | Categoría
--------------------------------------------------------------
1  | Manzanas     | Fruta fresca  | 50       | 0.5    | Alimentos
```

## Notas
- El ID del producto se genera automáticamente.
- Los datos persisten en el archivo `inventario.db`, por lo que estarán disponibles en futuras ejecuciones del programa.

## Autores
Este proyecto fue desarrollado para gestionar inventarios de manera eficiente utilizando Python y SQLite.

ß