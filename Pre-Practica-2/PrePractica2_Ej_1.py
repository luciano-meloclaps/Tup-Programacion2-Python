# Crear un programa que permita ingresar una lista de numeros al usuario y muestre por pantalla el maximo entre ambos numeros.
# Nota : Hacerlo con la función max(a,b) y luego con una comparación

# INICIO
lista = []

print("Cuantos numero desea ingresar: ")
num = int(input())

for i in range(num):
    x = 0
    print("Ingrese numero")
    x = int(input())
    lista.append(x)
    
print(lista)
print("El numero maximo es: ", max(lista))
# FIN
