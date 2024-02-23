# prueba_tecnica.py

# Pregunta 1:
# Escribe una función que tome una lista de números y devuelva la suma de los números pares en la lista.
def suma_numeros_pares(lista):
    suma = 0
    for num in lista:
        if num % 2 == 0:
            suma += num
    return suma

# Pregunta 2:
# Escribe una función que tome una cadena y devuelva True si es un palíndromo, False en caso contrario.
def es_palindromo(cadena):
    return cadena == cadena[::-1]

# Pregunta 3:
# Escribe una función que tome dos listas y devuelva una lista que contenga solo los elementos comunes entre ambas.
def elementos_comunes(lista1, lista2):
    return list(set(lista1) & set(lista2))

# Pregunta 4:
# Escribe una función que tome un número entero n y genere una lista de los primeros n números de la secuencia de Fibonacci.
def fibonacci(n):
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

# Pregunta 5:
# Escribe una función que tome una lista de palabras y devuelva la longitud de la palabra más larga en la lista.
def longitud_palabra_mas_larga(lista_palabras):
    return max(len(word) for word in lista_palabras)

# Pregunta 6 (Extra):
# Escribe una función que implemente el algoritmo de ordenamiento burbuja para ordenar una lista de números de menor a mayor.
def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

# Pregunta 7 (Extra):
# Escribe una función que tome un número entero n y devuelva una lista de los primeros n números primos.
def numeros_primos(n):
    def es_primo(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    primos = []
    num = 2
    while len(primos) < n:
        if es_primo(num):
            primos.append(num)
        num += 1
    return primos