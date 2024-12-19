class Producto():
    def __init__(self,id,nombre,descipcion,cantidad,precio,categoria):
        self.id = int(id)
        self.nombre = nombre.title()
        self.descripcion= descipcion
        self.cantidad = cantidad
        self.precio = precio
        self.categoria = self.comprobar_categoria(categoria)


    def comprobar_categoria(self, categoria):
        return "Sin Categoria" if categoria == "" else categoria.title()
