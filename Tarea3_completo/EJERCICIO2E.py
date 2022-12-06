from EJERCICIO2BASE import inventario
def borrartodo():
    if input("Seguro (s/n): ") == "s":
        inventario.nombres = []
        inventario.cantidades_ingresadas = []
        inventario.precios = []