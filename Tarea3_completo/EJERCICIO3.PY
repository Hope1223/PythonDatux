class Ejercicio3:
    class Animal:
        def __init__(self, nombre, color):
            self.nombre = nombre
            self.color=color
    class Perro(Animal):
        def sonido(self):
            print('El sonido que hace es ladrar')
    class Gato(Animal):
        def sonido(self):
            print('El sonido que hace es maullar')

    firulais=Perro('firulais','dorado')
    chispa=Gato('chispa','blanco')

    print(firulais.color)
    firulais.sonido()
    chispa.sonido()