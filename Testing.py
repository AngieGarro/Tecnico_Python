#Clase para hacer testing
#---------------------------------------------

# Definición de la función cuadrado
def cuadrado(numero):
    return numero ** 2

# Solicitar al usuario ingresar un número
numero = int(input("Por favor ingresa un número para calcular su cuadrado: "))

# Calcular el cuadrado utilizando la función cuadrado
resultado = cuadrado(numero)
print(f"El cuadrado de {numero} es: {resultado}")
