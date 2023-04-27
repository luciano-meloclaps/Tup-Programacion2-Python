"""Único return vs múltiples return."""

from typing import Union


def operacion_basica(a: float, b: float, multiplicar: bool) -> Union[float, str]:
    """Toma dos números (a, b) y un booleano (multiplicar):
        - Si multiplicar es True: devuelve la multiplicación entre a y b.
        - Si multiplicar es False: devuelve la division entre a y b.
        - Si multiplicar es False y b es cero: devuelve "Operación no válida".

    Restricciones:
        - Utilizar un único return.
        - Utilizar IF con ELIF con ELSE.
        - No utilizar AND ni OR.
    """

    if multiplicar:
        operacion_basica = a * b
    elif b == 0:
        operacion_basica = "Operación no válida"
    else:
        operacion_basica = a / b

    return operacion_basica


# NO MODIFICAR - INICIO
assert operacion_basica(1, 1, True) == 1
assert operacion_basica(1, 1, False) == 1
assert operacion_basica(25, 5, True) == 125
assert operacion_basica(25, 5, False) == 5
assert operacion_basica(0, 5, True) == 0
assert operacion_basica(0, 5, False) == 0
assert operacion_basica(1, 0, True) == 0
assert operacion_basica(1, 0, False) == "Operación no válida"

# IMPRIMIMOS
print("RESULTADO DE LAS OPERACIONES BASICAS ES: ", operacion_basica(1, 1, True))
# NO MODIFICAR - FIN


###############################################################################

def operacion_multiple(a: float, b: float, multiplicar: bool) -> Union[float, str]:  
    """Re-Escribir el ejercicio anterior utilizando tres returns.

    Restricciones:
        - Utilizar 2 IF.
        - No Utilizar IF anidados.
        - No utilizar ELIF ni ELSE.
        - No utilizar AND ni OR.
    """

    if multiplicar:
        operacion_multiple = a * b
        return operacion_multiple
    
    if b == 0:
        return "Operación no válida"
    
    operacion_multiple = a / b
    return operacion_multiple


# NO MODIFICAR - INICIO
assert operacion_multiple(1, 1, True) == 1
assert operacion_multiple(1, 1, False) == 1
assert operacion_multiple(25, 5, True) == 125
assert operacion_multiple(25, 5, False) == 5
assert operacion_multiple(0, 5, True) == 0
assert operacion_multiple(0, 5, False) == 0
assert operacion_multiple(1, 0, True) == 0
assert operacion_multiple(1, 0, False) == "Operación no válida"

# IMPRIMIMOS
print("RESULTADO DE LAS OPERACIONES MULTIPLES ES: ", operacion_multiple(1, 0, True))
# NO MODIFICAR - FIN
