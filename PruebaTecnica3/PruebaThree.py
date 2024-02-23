# prueba_tecnica.py

# Pregunta 1:
# Escribe una función que tome una lista de números enteros y devuelva el promedio de los números.
def calcular_promedio(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)

# Pregunta 2:
# Escribe una función que tome una cadena y devuelva la cadena con todas las vocales reemplazadas por '*'.
def reemplazar_vocales(cadena):
    vocales = 'aeiouAEIOU'
    for vocal in vocales:
        cadena = cadena.replace(vocal, '*')
    return cadena

# Pregunta 3:
# Escribe una función que tome una lista de números y devuelva la suma de los elementos que están en índices pares.
def suma_indices_pares(lista):
    return sum(lista[i] for i in range(len(lista)) if i % 2 == 0)

# Pregunta 4:
# Escribe una función que tome un número entero n y devuelva True si es un número primo, False en caso contrario.
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Pregunta 5:
# Escribe una función que tome una cadena y devuelva True si es un anagrama de 'roma', False en caso contrario.
def es_anagrama_de_roma(cadena):
    return sorted(cadena.lower()) == sorted('roma')

# Pregunta 6 (Extra):
# Escribe una función que tome una lista de números y devuelva la mediana de la lista.
# La mediana es el valor que está en la mitad de una lista ordenada.
def calcular_mediana(lista):
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    if n % 2 == 0:
        return (lista_ordenada[n // 2 - 1] + lista_ordenada[n // 2]) / 2
    else:
        return lista_ordenada[n // 2]

# Pregunta 7 (Extra):
# Escribe una función que tome una cadena y devuelva una lista de todas las palabras que tienen al menos 3 letras repetidas consecutivas.
def palabras_con_repetidas_consecutivas(cadena):
    palabras = cadena.split()
    palabras_con_repetidas = []
    for palabra in palabras:
        for i in range(len(palabra) - 2):
            if palabra[i] == palabra[i + 1] == palabra[i + 2]:
                palabras_con_repetidas.append(palabra)
                break
    return palabras_con_repetidas