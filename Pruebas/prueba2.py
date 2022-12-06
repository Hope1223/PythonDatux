from prueba1 import regresa
def registrar():
    nombre = input("Nombre del producto: ")
    cantidad = int(input("Cantidad vendida: "))
    precio = int(input("Precio del producto: "))

    regresa.nombres.append(nombre)
    regresa.precios.append(precio)
    regresa.cantidades_ingresadas.append(cantidad)
