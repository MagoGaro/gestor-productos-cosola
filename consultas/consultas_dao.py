from coneccion.conexion import ConneccionDB

def agregar_producto(producto):
    conn = ConneccionDB()

    sql= f'''
        INSERT INTO productos(nombre,descripcion,cantidad,precio,categoria)
        VALUES('{producto.nombre}','{producto.descripcion}',{producto.cantidad},{producto.precio},'{producto.categoria}');'''
    
    conn.cursor.execute(sql)
    conn.cerrar_con()

def modificar_producto(producto):
    conn = ConneccionDB()

    sql= f'''
        UPDATE productos
        SET nombre ='{producto.nombre}', 
        descripcion = '{producto.descripcion}', 
        cantidad ={producto.cantidad},
        precio = {producto.precio}, 
        categoria ='{producto.categoria}'
        WHERE id = {producto.id};'''
    
    conn.cursor.execute(sql)
    conn.cerrar_con()

def eliminar_producto(producto):
    conn = ConneccionDB()

    sql= f'''
        DELETE FROM productos
        WHERE id = {producto.id}
        ;'''
    
    conn.cursor.execute(sql)
    conn.cerrar_con()

def listar_producto():
    conn = ConneccionDB()

    listar_productos =[]

    sql= f'''
        SELECT * From productos;'''
    
    conn.cursor.execute(sql)
    listar_productos = conn.cursor.fetchall()

    conn.cerrar_con()

    return listar_productos

def obtener_encabezados():
    conn = ConneccionDB()
    
    sql= f'''
        SELECT * From productos;'''
    conn.cursor.execute(sql)

    encabezados = [desc[0] for desc in conn.cursor.description]
    conn.cerrar_con()

    return encabezados


def buscar_producto(id = None, nombre = None,categoria = None):
    conn = ConneccionDB()
    clausulas=[]
    parametros = []
    listar_productos=[]

    if id is not None:
        clausulas.append('id = ?')
        parametros.append(id)
    if nombre is not None:
        clausulas.append('nombre LIKE ?')  
        parametros.append(f'%{nombre}%')  
    if categoria is not None:
        clausulas.append('categoria LIKE ?')
        parametros.append(f'%{categoria}%')

    sql= f'''
        SELECT * From productos
        WHERE  {' OR '.join(clausulas)} ;'''

    conn.cursor.execute(sql,parametros)
    listar_productos = conn.cursor.fetchall()
    conn.cerrar_con()

    return listar_productos

def stock_productos(stock):
    conn = ConneccionDB()

    listar_productos =[]

    sql= f'''
        SELECT * From productos WHERE cantidad <= {stock};'''
    
    conn.cursor.execute(sql)
    listar_productos = conn.cursor.fetchall()

    conn.cerrar_con()

    return listar_productos