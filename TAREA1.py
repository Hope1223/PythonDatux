#EJERCICIO 1
apellidos1=input("Ingrese sus apellidos: ")
apellidos=apellidos1.upper()
nombres1=input("Ingrese sus nombres: ")
nombres=nombres1.upper()
#passaporte, dni, carnet de extranjeria.
while True:
    print("""Escribe una opcion"
            1) DNI
            2) Passaporte
            3) Carnet de extranjeria""")
    opcion=input()

    if opcion =='1':
        ID=int(input('Ingrese su dni: '))
        break
    elif opcion=='2':
        ID=int(input('Ingrese su dni: '))
        break
    elif opcion=='3':
        ID=int(input('Ingrese su carnet de extranjeria: '))
        break
    else:
       print('Ingrese una opcion valida')
edad=int(input('Ingrese su edad: '))
print(f'---------------------------------------')
print(f'Sus datos son: ')
print(f'Nombres: {nombres}, {apellidos}')
print(f'Documento de identificacion: {ID}')
print(f'Edad: {ID}')
print(f'---------------------------------------')

#EJERCICIO 2

import math as np
dato=""
while True:
    print("""Escribe una opcion"
            1) Radio
            2) Diametro""")
    opcion=input()

    if opcion =='1':
        dato=float(input('Ingrese el radio: '))
        area=(dato*dato)*(np.pi)
        break
    elif opcion=='2':
        dato=float(input('Ingrese el Diametro: '))
        area=((dato*dato)*(np.pi))/4
        break
    else:
        print("ingrese una opcion valida")  
print(f'El area es : ',{area})

#EJERCICIO 3

a=float(input("Ingrese un numero : "))
b=float(input("Ingrese un numero : "))
c=float(input("Ingrese un numero : "))

d=a+b+c
e=a-b-c
f=a*b*c
print('---------------------------')
print(f'La suma es : ',d)
print(f'La resta es : ',e)
print(f'La multiplicacion es : ',f)
print('---------------------------')

#EJERCICIO 4

a=input("Ingrese un numero : ")
	print(type(a))

	
#EJERCICIO 5
import sys
	variable = sys.argv[0]
	print(variable)

#EJERCICIO 6

x = int(input("Ingrese un numero : "))
y=0
for x in range(1, x+1):
    print(f'este numero se esta sumando: ',x)
    y=y+x
print(f"La suma total es: ",y)

#EJERCICIO 7

a=float(input("Ingrese un numero: "))
b=float(input("Ingrese un numero: "))
if a==b:
	print(f"El numero : ",a,"es igual a : ",b)
elif a!=b:
	print("Son numeros diferentes")
	if a>b:
		print(f"El numero : ", a ,"es mayor que : ", b)
	elif b>=a:
		print(f"El numero : " ,b, "es mayor que : " ,a)
#EJERCICIO 8

def ingresa(clave1):
    print("Vuelva ingresar su clave")
    clave=input()
    if clave==clave1:
        print("Coinciden su clave")
    else:
        print("No es la misma clave")
        return ingresa(clave1)

if __name__ == '__main__':
    clave1=input("Ingrese su clave: ")
    ingresar=ingresa(clave1)

#EJERCICIO 9

def parim(numero):
	if numero%2==1:
		print("El numero: ",numero, "es impar")
	else:
		print("El numero: ",numero, "es par")

if __name__ == '__main__':
    numero=int(input("Ingrese un numero: "))
    parim(numero)

#EJERCICIO 10

def ingresa(monto):
   
    n=int(input('Ingresar dias demorados: '))
    if n<=10 and n>=1:
        monto=monto*1.05
        print(f'La deuda acumulada es:', monto)
    elif n<=30:
        monto=monto*1.08
        print(f'La deuda acumulada es:', monto)
    elif n<=90:
        monto=monto*1.10
        print(f'La deuda acumulada es:', monto)
    else:
        print(f'Su deuda sera enviada al estado')
if __name__ == '__main__':
 monto=float(input('Ingresar la mensualidad: '))
 ingresa(monto)

#EJERCICIO 11
def check_float(str_input):
    # Verifica un string compuesto de numeros. Devuelve True si es, de lo contrario False.
    return str_input.lstrip('-').replace('.','',1).isdigit()
def opciones():
    while True:
        print(f'Ingresar 2 numeros')
        a=input('1er numero: ')
        b=input('2do numero: ')
        if (check_float(a) and check_float(b)) == False:
            print("Error, al menos una de las entradas no es un numero")
            continue
        else:        
            print("""Escribe una opcion"
                    1) Sumar
                    2) Restar
                    3) Multiplicar""")
            opcion=input()

            if opcion =='1':
                print(f'La suma es: ', float(a)+float(b))
                break
            elif opcion=='2':
                print(f'La suma es: ', float(a)-float(b))
                break
            elif opcion=='3':
                print(f'La suma es: ', float(a)*float(b))
                break
            else:
                print('Ingresar los numeros previsualizados')
if __name__ == '__main__':
    opciones()

#EJERCICIO 12
def vocal():
    letra=input("Ingresa una letra:")
    if len(letra)!=1:
        print("Debe ser solo una letra")
    elif len(letra)==1:
        if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
            print('Es vocal: ',letra )
        else:
            print('La letra es: ',letra)
if __name__ == '__main__':
    vocal()
#EJERCICIO 13

lista=["Carlo Gomez","Reynaldo Ferrero","Lorenzo Humbert","Marcelo Merino","Fernando Suarez"]
print("posicion final : ",lista[-1])
lista.reverse()
print(lista)

#EJERCICIO 14

#EJERCICIO 15

def opciones():
    while True:  
            print("""Escribe una opcion
                    1) Saludar
                    2) Operacion matematica
                    3) Salir""")
            opcion=input()

            if opcion =='1':
                print(f'Hola mundo')
            elif opcion=='2':
                while True:
                    print(f'Ingresar 2 numeros')
                    a=input('1er numero: ')
                    b=input('2do numero: ')   
                    print("""Escribe una opcion
                            1) Sumar
                            2) Restar
                            3) Multiplicar""")
                    opcion=input()

                    if opcion =='1':
                        print(f'La suma es: ', float(a)+float(b))
                        break
                    elif opcion=='2':
                        print(f'La suma es: ', float(a)-float(b))
                        break
                    elif opcion=='3':
                        print(f'La suma es: ', float(a)*float(b))
                        break
            elif opcion=='3':
                print(f'Saliendo...')
                break

if __name__ == '__main__':
    opciones()

#EJERCICIO 16

