#Crear un programa que permita al usuario ingresar una lista de numeros. De esa lista de numeros almacenar en otra lista los numeros impares.
#El programa debe de mostrar por pantalla la lista de numeros originales y la lista de numeros impares.

#INICIO
listaNum = []
listaImpar = []

print("Ingrese la cantidad de numero en la lista: ")
cant = int(input())
for i in range(cant):
    print("Ingrese un numero: ")
    num = int(input())
    listaNum.append(num)
    
    if num % 2 != 0:
        listaImpar.append(num)
        
print("La lista original es: ", listaNum)
print("La lista de numeros impares es: ", listaImpar)
#FIN