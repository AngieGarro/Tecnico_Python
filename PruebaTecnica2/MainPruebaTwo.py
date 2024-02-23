# Importar las funciones del archivo PruebaTwo.py
from PruebaTecnica2.PruebaTwo import *

def mostrar_menu():
    print("Menú:")
    print("1. Suma de números impares en una lista")
    print("2. Frecuencia de letras en una cadena")
    print("3. Ordenamiento personalizado de una lista")
    print("4. Verificar si una cadena es un pangrama")
    print("5. Verificar si un número es perfecto")
    print("6. Invertir el orden de las palabras en una cadena")
    print("7. Eliminar duplicados de una lista")
    print("0. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            lista = list(map(int, input("Ingrese una lista de números separados por espacios: ").split()))
            print("La suma de los números impares es:", suma_numeros_impares(lista))
        elif opcion == "2":
            cadena = input("Ingrese una cadena: ")
            print("Frecuencia de letras:")
            frecuencias = frecuencia_letras(cadena)
            for letra, frecuencia in frecuencias.items():
                print(f"{letra}: {frecuencia}")
        elif opcion == "3":
            lista = list(map(int, input("Ingrese una lista de números separados por espacios: ").split()))
            print("La lista ordenada de mayor a menor es:", ordenamiento_personalizado(lista))
        elif opcion == "4":
            cadena = input("Ingrese una cadena: ")
            if es_pangrama(cadena):
                print("La cadena es un pangrama.")
            else:
                print("La cadena no es un pangrama.")
        elif opcion == "5":
            n = int(input("Ingrese un número entero: "))
            if es_numero_perfecto(n):
                print("El número es perfecto.")
            else:
                print("El número no es perfecto.")
        elif opcion == "6":
            cadena = input("Ingrese una cadena de palabras separadas por espacios: ")
            print("La cadena con las palabras en orden inverso es:", invertir_palabras(cadena))
        elif opcion == "7":
            lista = list(map(int, input("Ingrese una lista de números separados por espacios: ").split()))
            print("La lista con duplicados eliminados es:", eliminar_duplicados(lista))
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
