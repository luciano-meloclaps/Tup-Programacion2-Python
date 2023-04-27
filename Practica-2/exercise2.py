"""Comparaciones Encadenadas, Cantidad Arbitraria de Parámetros, Recursividad.
"""


def maximo_encadenado(a: float, b: float, c: float) -> float:
    """Toma 3 números y devuelve el máximo.

    Restricciones:
        - Utilizar comparaciones encadenadas.
        - Utilizar UNICAMENTE dos IFs
        - No utilizar ELSE
        - No utilizar AND, OR o NOT

    Referencia: https://docs.python.org/3/reference/expressions.html#comparisons # noqa: E501
    """

    if a >= b >= c:
        return max(a, b, c)

    if b >= c >= a:
        return max(b, c, a)

    return max(b, c, a)


# NO MODIFICAR - INICIO
assert maximo_encadenado(1, 10, 5) == 10
assert maximo_encadenado(5, 10, 1) == 10
assert maximo_encadenado(5, 10, 5) == 10

assert maximo_encadenado(4, 9, 18) == 18
assert maximo_encadenado(9, 4, 18) == 18
assert maximo_encadenado(9, 9, 18) == 18

assert maximo_encadenado(24, 9, 18) == 24
assert maximo_encadenado(24, 18, 9) == 24
assert maximo_encadenado(24, 18, 18) == 24


# IMPRIMIMOS
print("RESULTADOS DE LOS MAXIMOS ENCADENADOS: ", maximo_encadenado(1, 10, 5), maximo_encadenado(5, 10, 1), maximo_encadenado(5, 10, 5), maximo_encadenado(
    4, 9, 18), maximo_encadenado(9, 4, 18), maximo_encadenado(9, 9, 18), maximo_encadenado(24, 9, 18), maximo_encadenado(24, 18, 9), maximo_encadenado(24, 18, 18))
print()
# NO MODIFICAR - FIN


def maximo_cuadruple(a: float, b: float, c: float, d: float) -> float:
    """Re-escribir para que tome 4 parámetros, utilizar la función max.
    Referencia: https://docs.python.org/3/library/functions.html#max"""

    return max(a, b, c, d)

# NO MODIFICAR - INICIO


assert maximo_cuadruple(1, 10, 5, -5) == 10
assert maximo_cuadruple(4, 9, 18, 6) == 18
assert maximo_cuadruple(24, 9, 18, 20) == 24
assert maximo_cuadruple(24, 9, 18, 30) == 30

# IMPRIMIMOS
print("EL MAXIMO CUADRUPLE DEl 1ro ES: ", maximo_cuadruple(1, 10, 5, -5))
print("EL MAXIMO CUADRUPLE DEl 2do ES: ", maximo_cuadruple(4, 9, 18, 6))
print("EL MAXIMO CUADRUPLE DEl 3ro ES: ", maximo_cuadruple(24, 9, 18, 20))
print("EL MAXIMO CUADRUPLE DEl 4to ES: ", maximo_cuadruple(24, 9, 18, 30))
print()
# NO MODIFICAR - FIN

###############################################################################


def maximo_arbitrario(*args) -> float:
    """Re-escribir para que tome una cantidad arbitraria de parámetros.
    Referencia: https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists # noqa: E501
    """

    return max(args)

# NO MODIFICAR - INICIO


assert maximo_arbitrario(1, 10, 5, -5) == 10
assert maximo_arbitrario(4, 9, 18, 6) == 18
assert maximo_arbitrario(24, 9, 18, 20) == 24
assert maximo_arbitrario(24, 9, 18, 30) == 30

# IMPRIMIMOS
print("EL MAXIMO ARBITRARIO DEL 1RO ES: ", maximo_arbitrario(5, 10, 1))
print("EL MAXIMO ARBITRARIO DEL 2DO ES: ", maximo_arbitrario(4, 9, 18, 6))
print("EL MAXIMO ARBITRARIO DEL 3RO ES: ", maximo_arbitrario(24, 9, 18, 20, 30))
# NO MODIFICAR - FIN
