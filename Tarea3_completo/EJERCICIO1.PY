class Ejercicio1:
    class Fruta:
        def __init__(self,nombre):
            self.nombre=nombre
        def __str__(self):
            return f'se llama {self.nombre}'

    f1=Fruta("Fresa")
    print(f1.nombre)
    print(f1)
