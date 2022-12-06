from EJERCICIO2BASE import inventario
def salidas():
    nombre_articulo = input("Nombre del articulo que se vende: ")
    if nombre_articulo in inventario.nombres:
        cantidad = int(input("Cantidad vendida: "))
        indice = inventario.nombres.index(nombre_articulo)
        precio = inventario.precios[indice]
        inventario.cantidades_ingresadas[indice] -= cantidad
        print(
            f"Se vende(n) {cantidad} {nombre_articulo}. Total: S/. {cantidad * precio}")
    else:
        print("El articulo no existe")