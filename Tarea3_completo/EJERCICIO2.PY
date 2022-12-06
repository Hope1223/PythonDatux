class Ejercicio2:
    import sys
    from EJERCICIO2C import registrar
    from EJERCICIO2D import mostrar
    from EJERCICIO2E import borrartodo
    from EJERCICIO2A import entradas
    from EJERCICIO2B import salidas
    from EJERCICIO2BASE import inventario
    while True:
        try:
            print("""
            1 - Ingresar un articulo nuevo
            2 - Ver el inventario
            3 - Registrar Entrada
            4 - Registrar Salida
            5 - Borrar todos los articulos
            6 - Salir
            Seleccione: """)
            opcion=int(input("Ingrese un numero: "))
        except ValueError:
            print("Ingrese una opcion valida")
        else:
            if opcion<1 and opcion>4:
                print("No es una opcion valida")
                continue
            if opcion==1:
                registrar()
            elif opcion==2:
                mostrar()
            elif opcion==3:
                entradas()
            elif opcion==4:
                salidas()
            elif opcion==5:
                borrartodo()
            else:
                break
    print("Vuelva pronto")