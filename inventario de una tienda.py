class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def actualizar_stock(self, cantidad):
        self.stock += cantidad

    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Precio: {self.precio}, Stock: {self.stock}"
    
    def aplicar_iva(self):
        self.precio *= 1.19


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def aplicar_iva_a_productos(self):
        for producto in self.productos:
            producto.aplicar_iva()

    def buscar_producto(self, codigo):
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
        return None

    def mostrar_inventario(self):
        print("Inventario:")
        for producto in self.productos:
            print(producto)

    def generar_informe(self):
        total_valor_inventario = 0
        for producto in self.productos:
            total_valor_inventario += producto.precio * producto.stock
        return total_valor_inventario


class Venta:
    def __init__(self, inventario):
        self.inventario = inventario
        self.carrito = []

    def agregar_producto(self, codigo, cantidad):
        producto = self.inventario.buscar_producto(codigo)
        if producto is not None and producto.stock >= cantidad:
            self.carrito.append((producto, cantidad))
            producto.actualizar_stock(-cantidad)
            print(f"Producto '{producto.nombre}' agregado al carrito.")
        else:
            print("No hay suficiente stock disponible.")

    def aplicar_iva_a_carrito(self):
        for producto, _ in self.carrito:
            producto.aplicar_iva()

    def mostrar_carrito(self):
        print("Carrito:")
        for producto, cantidad in self.carrito:
            print(f"Producto: {producto.nombre}, Cantidad: {cantidad}")

    def generar_total_venta(self):
        total_venta = 0
        for producto, cantidad in self.carrito:
            total_venta += producto.precio * cantidad
        return total_venta



inventario = Inventario()

producto1 = Producto("P1", "Camisa", 25.0, 10)
producto2 = Producto("P2", "Pantalón", 40.0, 5)
producto3 = Producto("P3", "Zapatos", 60.0, 3)

inventario.agregar_producto(producto1)
inventario.agregar_producto(producto2)
inventario.agregar_producto(producto3)


inventario.mostrar_inventario()


venta = Venta(inventario)
venta.agregar_producto("P1", 2)
venta.agregar_producto("P2", 1)
venta.agregar_producto("P3", 2)
venta.agregar_producto("P3", 2)  


venta.mostrar_carrito()


total_venta = venta.generar_total_venta()
print(f"Total de la venta: {total_venta}")


inventario.mostrar_inventario()


total_valor_inventario = inventario.generar_informe()
print(f"Total valor del inventario: {total_valor_inventario}")

inventario.aplicar_iva_a_productos()
inventario.mostrar_inventario()
total_venta_con_iva = venta.generar_total_venta()
print(f"Total de la venta con IVA: {total_venta_con_iva}")