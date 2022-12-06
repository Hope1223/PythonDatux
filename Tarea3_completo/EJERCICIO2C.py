from EJERCICIO2BASE import inventario
def registrar():
    nombre = input("Nombre del producto: ")
    cantidad = int(input("Cantidad registrada: "))
    precio = int(input("Precio del producto: "))
    inventario.nombres.append(nombre)
    inventario.precios.append(precio)
    inventario.cantidades_ingresadas.append(cantidad)
