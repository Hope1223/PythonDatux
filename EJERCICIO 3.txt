#EJERCICIO 1

class Fruta:
    def __init__(self,nombre):
        self.nombre=nombre
    def __str__(self):
        return f'se llama {self.nombre}'

f1=Fruta("Fresa")
print(f1.nombre)
print(f1)

------------------------------------
#EJERCICIO 3

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

------------------------------------
#EJERCICIO 5

import sys
variable = sys.argv[0]
print(variable)

------------------------------------
#EJERCICIO 6

import random
numerorand=random.randrang(1,100)
print(numerorand)

------------------------------------
#EJERCICIO 7

import requests
from datetime import datetime
now = datetime.now()
url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat' 

response = requests.get(url)

response.json() 
dolar=response.json()
dolar_compra = dolar['compra']
dolar_venta = dolar['venta']

print("Precio compra del dolar :",dolar_compra)
print("Precio venta del dolar  :",dolar_venta)
print("Fecha                   :", now)

------------------------------------
#EJERCICIO 8
#EJERCICIO 9
import re
cadena ='Python es uno de los lenguajes de programacion dinamicos mas populares que existen entre los que se encuentran Java,Javascript, Go y C#. Aunque es considerado a menudo como un lenguaje "scripting", es realmente un lenguaje de proposito general. En la actualidad, Python es usado para todo, desde simples "scripts", hasta grandes servidores web que proveen servicio ininterrumpido 24Å~7. Es utilizado para la programacion de interfaces graficas y bases de datos, programacion web tanto en el cliente como en el servidor (vease Django o Flask) y "testing" de aplicaciones'.upper()
#buscar=input("Ingresar una palabra para buscar: ")
buscar="PYTHON"
busqueda=re.search(buscar,cadena)
if busqueda:
    print("Si se encontro")
else:
    print("No se encontro")

print("La palabra" ,buscar, "se repite: ",cadena.count(buscar), "veces")

