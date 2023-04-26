"""Bloque IF, operadores lógicos, función max y operador ternario."""


def maximo_basico(a: float, b: float) -> float:
    """Toma dos números y devuelve el mayor.

    Restricciones:
        - Utilizar IF
        - No utilizar ELSE
        - No utilizar la función max
    """
    a = float(a)
    b = float(b)

    if a > b:
        return a
    if b > a:
        return b
    return a


# NO MODIFICAR - INICIO
assert maximo_basico(10, 5) == 10
assert maximo_basico(9, 18) == 18
print("MAXIMO BASICO A: ", maximo_basico(10, 5))
print("MAXIMO BASICO B: ", maximo_basico(9, 18))
print()
# NO MODIFICAR - FIN

###############################################################################


def maximo_libreria(a: float, b: float) -> float:
    """Re-escribir utilizando el built-in max.
    Referencia: https://docs.python.org/3/library/functions.html#max
    """

    a = float(a)
    b = float(b)
    return max(a, b)


# NO MODIFICAR - INICIO
assert maximo_libreria(10, 5) == 10
assert maximo_libreria(9, 18) == 18
print("MAXIMO LIBRERIA A: ", maximo_libreria(10, 5))
print("MAXIMO LIBRERIA B: ", maximo_libreria(9, 18))
print()

# NO MODIFICAR - FIN


###############################################################################


def maximo_ternario(a: float, b: float) -> float:
    """Re-escribir utilizando el operador ternario.
    Referencia: https://docs.python.org/3/reference/expressions.html#conditional-expressions # noqa: E501
    """

    a = float(a)
    b = float(b)
    maximo_ternario = a if a > b else b
    return maximo_ternario


# NO MODIFICAR - INICIO
assert maximo_ternario(10, 5) == 10
assert maximo_ternario(9, 18) == 18
print("MAXIMO TERNARIO A: ", maximo_ternario(10, 5))
print("MAXIMO TERNARIO B: ", maximo_ternario(9, 18))
print()


# NO MODIFICAR - FIN
