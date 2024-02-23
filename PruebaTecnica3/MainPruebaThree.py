# Importar las funiones PruebaThree.py
from PruebaThree import *

def mostrar_menu():
    print("Menú:")
    print("1. Calcular promedio de una lista de números")
    print("2. Reemplazar vocales por '*' en una cadena")
    print("3. Suma de elementos en índices pares de una lista")
    print("4. Verificar si un número es primo")
    print("5. Verificar si una cadena es un anagrama de 'roma'")
    print("6. Calcular mediana de una lista de números")
    print("7. Encontrar palabras con letras repetidas consecutivas en una cadena")
    print("0. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            lista = list(map(int, input("Ingrese una lista de números separados por espacios: ").split()))
            print("El promedio de la lista es:", calcular_promedio(lista))
        elif opcion == "2":
            cadena = input("Ingrese una cadena: ")
            print("La cadena con las vocales reemplazadas es:", reemplazar_vocales(cadena))
        elif opcion == "3":
            lista = list(map(int, input("Ingrese una lista de números separados por espacios: ").split()))
            print("La suma de los elementos en índices pares es:", suma_indices_pares(lista))
        elif opcion == "4":
            n = int(input("Ingrese un número entero: "))
            if es_primo(n):
                print("El número es primo.")
            else:
                print("El número no es primo.")
        elif opcion == "5":
            cadena = input("Ingrese una cadena: ")
            if es_anagrama_de_roma(cadena):
                print("La cadena es un anagrama de 'roma'.")
            else:
                print("La cadena no es un anagrama de 'roma'.")
        elif opcion == "6":
            lista = list(map(float, input("Ingrese una lista de números separados por espacios: ").split()))
            print("La mediana de la lista es:", calcular_mediana(lista))
        elif opcion == "7":
            cadena = input("Ingrese una cadena: ")
            print("Palabras con letras repetidas consecutivas:", palabras_con_repetidas_consecutivas(cadena))
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
