from EJERCICIO2BASE import inventario
def entradas(): 
    nombre_articulo = input("Nombre del articulo que se ingresada: ")
    if nombre_articulo in inventario.nombres:
        cantidad = int(input("Cantidad ingresada: "))
        indice = inventario.nombres.index(nombre_articulo)
        precio = inventario.precios[indice]
        inventario.cantidades_ingresadas[indice] += cantidad
        print(
            f"Se ingresa(n) {cantidad} {nombre_articulo}. Total: S/. {cantidad * precio}")
    else:
        print("El articulo no existe")