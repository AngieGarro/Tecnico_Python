# prueba_tecnica.py
#Imprimir:
print('Ejecutando prueba técnica...')

#Tipos de Datos
print(type("Hola"))  #Cadena (string)
print(type(123))    #Entero (int)
print(type(1.5))    #Flotante (float)
print(type(True))   #Booleano (bool)

#Operadores Aritméticos & Variables
numero = 7
otroNumero = 3
suma = numero + otroNumero
resta = numero - otroNumero
multiplicacion = numero * otroNumero
division = numero / otroNumero
divisionFlor = numero // otroNumero #Borra los decimales y lo devuelve en entero.
potenciacion = numero ** otroNumero #Exponente.
modulo = numero % otroNumero  #Resto, es el residuo de una division.
print("Suma: ", suma, "\nResta: ", resta, "\nMultiplicación: ", multiplicacion, "\nDivisión: ", division, "\nPotenciación: ", potenciacion, "\nMódulo: ", modulo)

#Operadores comparativos
print(numero == otroNumero) #Igualdad
print(numero != otroNumero) #Desigualdad o distinto
print(numero > otroNumero)  #Mayor que
print(numero < otroNumero)  #Menor que
print(numero >= otroNumero) #Mayor o igual a
print(numero <= otroNumero) #Menor o igual a

#Asignación
numero += otroNumero     #Agregar a la variable "numero" el valor de "otronumero".
numero -= otroNumero          
numero *= otroNumero               
numero /= otroNumero         #Es como hacer "numero = numero/otronumero", pero con asignación.

#Bucle while
contador = 0
while contador < 5 :
    print("Contador: ", contador)
    contador += 1

#Bucle for
for i in range(6):
    print("Valor de I: ", i)

#Break y continue
numerosPares = [2,4,6,8]
for n in numerosPares:
    if n%2==0:
        print(n,"es par.")
        break   #Sale del bucle al encontrar un número par.
    else:
        print(n,"es impar.")
        continue #Vuelve al principio del bucle si encuentra un número impar.   
    #Listas
    listaNumeros = [1,3,7,9]
    for num in listaNimeros:
        print("El número", num, "está en la posición", listaNumeros.index(num))
    
    