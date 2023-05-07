"""For, Sum, Reduce."""


def sumatoria_basico(n: int) -> int:
    """Devuelve la suma de los números de 1 a N.

    Restricción: Utilizar un bucle FOR.
    """

    lista = range(1, n+1)
    suma = 0

    for i in lista:
        suma += i

    return suma


# NO MODIFICAR - INICIO
assert sumatoria_basico(1) == 1
assert sumatoria_basico(100) == 5050

# IMPRIMIMOS
print("EJERCICIO 1:", sumatoria_basico(1))
print("EJERCICIO 1:", sumatoria_basico(100))
print("\n")
# NO MODIFICAR - FIN


###############################################################################


def sumatoria_sum(n: int) -> int:
    """Re-Escribir utilizando la función sum.

    Restricción: No utilizar bucles (FOR, WHILE, etc)
    Referencia: https://docs.python.org/3/library/functions.html#sum
    """
    lista = range(1, n+1)
    resultado = sum(lista)
    return resultado

# NO MODIFICAR - INICIO
assert sumatoria_sum(1) == 1
assert sumatoria_sum(100) == 5050

# IMPRIMIMOS
print("EJERCICIO 2:", sumatoria_sum(1))
print("EJERCICIO 2:", sumatoria_sum(100))
print("\n")
# NO MODIFICAR - FIN


###############################################################################


from typing import Iterable

def multiplicar_basico(numeros: Iterable[float]) -> float:
    """Toma un lista de números y devuelve el producto todos los númereos. Si
    la lista está vacia debe devolver 0.

    Restricciones:
        - No usar bibliotecas auxiliares (Numpy, math, pandas).
        - Utilizar un bucle FOR
        - Utilizar múltiples Return
        - No utilizar ELSE
    """
    
    producto = 1
    for num in numeros:
        producto *= num
        if num == 0:
            return 0
    return producto if numeros else 0

# NO MODIFICAR - INICIO
assert multiplicar_basico([1, 2, 3, 4]) == 24
assert multiplicar_basico([2, 5]) == 10
assert multiplicar_basico([]) == 0
assert multiplicar_basico([1, 2, 3, 0, 4, 5]) == 0

#IMPRIMIMOS
print("EJERCICIO 3:", multiplicar_basico([1, 2, 3, 4]))  # debe imprimir 24
print("EJERCICIO 3:", multiplicar_basico([2, 5]))  # debe imprimir 10
print("EJERCICIO 3:", multiplicar_basico([]))  # debe imprimir 0
print("EJERCICIO 3:", multiplicar_basico([1, 2, 3, 0, 4, 5]))  # debe imprimir 0

# NO MODIFICAR - FIN
