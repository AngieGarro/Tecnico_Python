# Importar las funiones PruebaOne.py
from PruebaTecnica1.PruebaOne import *

def mostrar_menu():
    print("Menú:")
    print("1. Suma de números pares en una lista")
    print("2. Verificar si una cadena es un palíndromo")
    print("3. Elementos comunes entre dos listas")
    print("4. Generar los primeros n números de la secuencia de Fibonacci")
    print("5. Longitud de la palabra más larga en una lista")
    print("6. Ordenar una lista de números usando el algoritmo de ordenamiento burbuja")
    print("7. Generar los primeros n números primos")
    print("0. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            lista = list(map(int, input("Ingrese una lista de números separados por espacios: ").split()))
            print("La suma de los números pares es:", suma_numeros_pares(lista))
        elif opcion == "2":
            cadena = input("Ingrese una cadena: ")
            if es_palindromo(cadena):
                print("La cadena es un palíndromo.")
            else:
                print("La cadena no es un palíndromo.")
        elif opcion == "3":
            lista1 = list(map(int, input("Ingrese la primera lista de números separados por espacios: ").split()))
            lista2 = list(map(int, input("Ingrese la segunda lista de números separados por espacios: ").split()))
            print("Los elementos comunes son:", elementos_comunes(lista1, lista2))
        elif opcion == "4":
            n = int(input("Ingrese el número de términos de la secuencia de Fibonacci: "))
            print("La secuencia de Fibonacci es:", fibonacci(n))
        elif opcion == "5":
            lista_palabras = input("Ingrese una lista de palabras separadas por espacios: ").split()
            print("La longitud de la palabra más larga es:", longitud_palabra_mas_larga(lista_palabras))
        elif opcion == "6":
            lista = list(map(int, input("Ingrese una lista de números separados por espacios: ").split()))
            print("La lista ordenada es:", ordenamiento_burbuja(lista))
        elif opcion == "7":
            n = int(input("Ingrese el número de números primos que desea generar: "))
            print("Los primeros", n, "números primos son:", numeros_primos(n))
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()