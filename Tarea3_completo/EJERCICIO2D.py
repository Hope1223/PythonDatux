from EJERCICIO2BASE import inventario
def mostrar():
    if len(inventario.nombres) <= 0:
        print("No hay articulos")
        return

    print("|NOMBRE              |CANT.     |PRECIO    |IMPORTE   |")
    indice = 0
    total = 0
    while indice < len(inventario.nombres):
        nombre = inventario.nombres[indice]
        precio = inventario.precios[indice]
        cantidad_ingresada = inventario.cantidades_ingresadas[indice]
        importe = precio * cantidad_ingresada

        print("|{:<20}|{:>10.2f}|{:>10.2f}|{:>10.2f}|".format(
            nombre, cantidad_ingresada, precio, importe))
        print("+--------------------+----------+----------+----------+")
        total += importe
        indice += 1

    print(
        "|--------------------|----------|TOTAL:   S/. |{:>10.2f}|".format(total))
