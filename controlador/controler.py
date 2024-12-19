from .base_producto import Producto
from consultas.consultas_dao import *
import os
import re

def limpiar_pantalla():
    if os.name == 'nt':  # Si es Windows
        os.system('cls')
    else:  # Si es Linux/macOS
        os.system('clear')

def comprobar_string(cadena):
    patron = r'^[a-zA-Z ]+$'
    return bool(re.match(patron, cadena))

def confirmar(mensaje):
    while True:
        respuesta = input(f"{mensaje} (s/n): ").lower()
        if respuesta == 's':
            return True
        elif respuesta == 'n':
            return False
        else:
            print("Respuesta inválida. Por favor, ingrese 's' para sí o 'n' para no.")

def generar_tabla(listado,encabezado):
    max_longitudes = [max(len(str(celda)) for celda in columna) for columna in zip(*listado)]

    longitud_total = sum(max_longitudes) + len(max_longitudes) *4 - 1

    #titulo de la tabla
    titulo = "Tabla de Productos".center(longitud_total)
    print(titulo)
    print('-' * longitud_total)

    # Imprimir los encabezados
    for i, columna in enumerate(encabezado):
        print(f"{columna:^{max_longitudes[i]}}", end=' | ')
    print()

    # Imprimir una línea divisoria
    print('-' * longitud_total)

    # Imprimir la tabla
    for fila in listado:
        for i, celda in enumerate(fila):
            print(f"{celda:<{max_longitudes[i]}}", end=" | ")
        print()

def producto_agregar(estado, producto = None):
    if estado:
        print("Ingrese los datos del nuevo producto\n")
    else: 
        print("Ingrese los nuevos datos del producto\n")

    while True:
        nombre = input("Ingrese nombre del producto: ")

        if nombre == "" and estado:
            print("El nombre no puede quedar vacio.")
        else:
            if not estado and nombre != '':
                producto.nombre = nombre.title()
            break

    descripcion = input("Ingrese una descipcion para el producto: ")
    if not estado and descripcion != '':
        producto.descripcion = descripcion

    while True:
        cantidad = input("Ingrese cantidad del producto: ")

        if cantidad != "":
            if cantidad.isdigit():
                producto.cantidad = cantidad
                break
            else:
                print("La cantidad debe serun numero entero.")
        else:
            if not estado:
                break
            else:
                print("La cantidad no puede quedar vacia.")

    while True:
        precio = input("Ingrese precio del producto: ")

        if precio != "":
            try:
                precio = float(precio)
                producto.precio = precio
                break
            except:
                print("El precio debe serun numero real.")
        else:
            if not estado:
                break
            else:
                print("El precio no puede quedar vacio.")

    
    categoria = input("Ingrese una categoria para el producto: ")
    if not estado and categoria != '':
        producto.categoria = categoria.title()

    if estado:
        agregar_producto(Producto('',nombre,descripcion,cantidad, precio,categoria))
        print("\nProducto agregado correctamente\n")
    else:
        modificar_producto(producto)
        print("\nProducto modificado correctamente\n")

    input("Presiona Enter para continuar...\n")
    limpiar_pantalla()


def producto_mostrar():
    limpiar_pantalla()
    
    generar_tabla(listar_producto(),obtener_encabezados())
    
    input("\nPresiona Enter para continuar...\n")
    limpiar_pantalla()

def producto_buscar(retornar):
    
    datos = [None,None,None]

    while True:
        dato = input("\nIngrese el id, nombre o categoria del producto: ")

        if dato != "":
            if dato.isdigit():
                datos[0] = int(dato)
                break
            elif comprobar_string(dato):
                datos[1] = dato
                datos[2] = dato
                break
            else:
                print("El valor ingresado es incorrecto.")
        else:
            print("Debe ingresar al menos uno de los 3 datos.")

    if retornar:
            return datos

    generar_tabla(buscar_producto(*datos),obtener_encabezados())
    input("\nPresiona Enter para continuar...\n")
    limpiar_pantalla()

def producto_actualizar():
    while True:
        datos = producto_buscar(True)
        
        if len(buscar_producto(*datos)) > 1:
            print("\nHay demasidos productos, sea mas especifico en su busqueda.")
        else:
            producto = Producto(*buscar_producto(*datos)[0])
        
            print(f"\nA continuación editaremos el prudocto: {producto.nombre}\n")
            print(f'Si no desea modificar el dato, pulse la tecla "Enter"\n')

            producto_agregar(False, producto)
            break

def producto_eliminar():
    while True:
        datos = producto_buscar(True)
        
        if len(buscar_producto(*datos)) > 1:
            print("\nHay demasidos productos, sea mas especifico en su busqueda.")
        else:
            producto = Producto(*buscar_producto(*datos)[0])

            if confirmar(f"¿Estás seguro de eliminar el producto: {producto.nombre} ?"):
                eliminar_producto(producto)
                print("\nProducto Eliminado correctamente")
            break

def mostrar_stock():
    while True:
        cantidad = input("\nIngrese valor del stock que desea consultar: ")

        if cantidad !='':
            if cantidad.isdigit():
                cantidad = int(cantidad)
                break
            else:
                print("El valor ingresado es incorrecto")      
        else:
            print("La cantidad no puede estar vacia.")
    
    print()
    generar_tabla(stock_productos(cantidad),obtener_encabezados())
    input("\nPresiona Enter para continuar...\n")
    limpiar_pantalla()