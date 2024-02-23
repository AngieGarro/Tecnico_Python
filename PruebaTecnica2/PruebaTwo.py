# prueba_tecnica.py

# Pregunta 1:
# Escribe una función que tome una lista de números enteros y devuelva la suma de los números impares.
def suma_numeros_impares(lista):
    return sum(num for num in lista if num % 2 != 0)

# Pregunta 2:
# Escribe una función que tome una cadena y devuelva el número de veces que aparece cada letra en la cadena.
# El resultado debe ser un diccionario donde las claves son las letras y los valores son las frecuencias.
# Ignora mayúsculas y minúsculas (considera que 'A' y 'a' son lo mismo).
def frecuencia_letras(cadena):
    frecuencias = {}
    cadena = cadena.lower()
    for letra in cadena:
        if letra.isalpha():
            frecuencias[letra] = frecuencias.get(letra, 0) + 1
    return frecuencias

# Pregunta 3:
# Escribe una función que tome una lista de números y devuelva una lista con los elementos ordenados de mayor a menor.
# No utilices funciones de ordenamiento predefinidas.
def ordenamiento_personalizado(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] < lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista

# Pregunta 4:
# Escribe una función que tome una cadena y devuelva True si es un pangrama, False en caso contrario.
# Un pangrama es una frase que contiene todas las letras del alfabeto al menos una vez.
# Ignora mayúsculas y minúsculas (considera que 'A' y 'a' son lo mismo).
def es_pangrama(cadena):
    alfabeto = set("abcdefghijklmnopqrstuvwxyz")
    cadena = cadena.lower()
    return alfabeto.issubset(set(cadena))

# Pregunta 5:
# Escribe una función que tome un número entero n y devuelva True si es un número perfecto, False en caso contrario.
# Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos (excluyendo al propio número).
# Por ejemplo, 28 es un número perfecto porque 28 = 1 + 2 + 4 + 7 + 14.
def es_numero_perfecto(n):
    if n <= 0:
        return False
    suma_divisores = sum(divisor for divisor in range(1, n) if n % divisor == 0)
    return suma_divisores == n

# Pregunta 6 (Extra):
# Escribe una función que tome una cadena de palabras separadas por espacios y devuelva la misma cadena pero con las palabras en orden inverso.
def invertir_palabras(cadena):
    palabras = cadena.split()
    return ' '.join(palabras[::-1])

# Pregunta 7 (Extra):
# Escribe una función que tome una lista de números y devuelva una lista con los números duplicados eliminados, manteniendo el orden original.
def eliminar_duplicados(lista):
    lista_sin_duplicados = []
    for elemento in lista:
        if elemento not in lista_sin_duplicados:
            lista_sin_duplicados.append(elemento)
    return lista_sin_duplicados