# Crear un programa que utilice la estructura try - catch. El usuario debe de ingresar dos numeros y mostrar por pantalla
# el resultado de la división entre ambos numeros.
# En caso de que el divisor sea 0 utilizar la excepción ZeroDivisionError y mostrar el error por pantalla.

# INICIO
print("Ingrese el primer numero: ")
num1 = int(input())

print("Ingrese el segundo numero: ")
divisor = int(input())

try:
    num1 / divisor
    print("El resultado es: ", num1 / divisor)
except ZeroDivisionError:
    print("ERROR: No se puede dividir por cero")
# FIN
