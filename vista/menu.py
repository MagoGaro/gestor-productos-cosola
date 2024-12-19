import sys
from controlador.controler import *

def menu_principal():
    while True:
        opcion = input("""
                       Menú Principal:
                       1- Agregar Producto
                       2- Mostrar Productos
                       3- Actualizar Producto
                       4- Eliminar Producto
                       5- Buscar Productos
                       6- Reporte Stock
                       7- Salir
                       
                       Seleccione una Opcion:""")

        match opcion:
            case '1':
                producto_agregar(True)
            case '2':
                producto_mostrar()
            case '3':
                producto_actualizar()
            case '4':
                producto_eliminar()
            case '5':
                producto_buscar(False)
            case '6':
                mostrar_stock()
            case '7':
                print("Saliendo del programa...")
                sys.exit(0)
            case _:
                print("Opción inválida intente nuevamente")