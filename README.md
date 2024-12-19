# Gestor Productos

---

#### Ejecutar Aplicación:

Debe ejecutar el archivo **main.py** dentro del directorio raiz

---

#### Funcionalidades Aplicación:

* Agregar Productos
* Listar Productos
* Editar Productos
* Modificar Productos
* Eliminar Productos
* Reporte Stock
---
#### Mapa Aplicación:
```bash
├── directorio_raiz
│   ├── coneccion
│   │   ├── __init__.py
│   │   └── conexion.py
│   ├── consultas
│   │    ├── __init__.py
│   │    └── consultas_dao.py
│   ├── controlador
│   │    ├── __init__.py
│   │    ├── base_producto.py
│   │    └── controler.py
│   ├── ddbb
│   │   └── inventario.db
│   ├── vista
│   │    ├── __init__.py
│   │    └── menu.py
│   └── main.py
```
Los archivos **__init__.py** indican que esas carpetas son modulos de mi aplicación.

En la carpeta **coneccion**, se encuentra la coneccion a la base de datos.

En la carpeta **consultas**, se encuentran las diferentes consultas a la base de datos.

En la carpeta **controler**, se encuentra la plantilla base de procuto y todas la logica del programa.

En la carpeta **ddbb**, se encuentra la base de datos SQLlite.

En la carpeta **vista**, se encuentra el menú del programa.

El archivo **main.py**, es el archivo principal de la aplicación.