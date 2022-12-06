class Ejercicio8:
    import re
    cadena ='Python es uno de los lenguajes de programacion dinamicos mas populares que existen entre los que se encuentran Java,Javascript, Go y C#. Aunque es considerado a menudo como un lenguaje "scripting", es realmente un lenguaje de proposito general. En la actualidad, Python es usado para todo, desde simples "scripts", hasta grandes servidores web que proveen servicio ininterrumpido 24×7. Es utilizado para la programacion de interfaces graficas y bases de datos, programacion web tanto en el cliente como en el servidor (vease Django o Flask) y "testing" de aplicaciones'.upper()
    #buscar=input("Ingresar una palabra para buscar: ")
    buscar="PYTHON"
    busqueda=re.search(buscar,cadena)
    if busqueda:
        print("Si se encontro")
    else:
        print("No se encontro")

