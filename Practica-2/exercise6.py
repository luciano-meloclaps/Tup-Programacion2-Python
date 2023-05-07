"""Type, Comprensión de Listas, Sorted y Filter."""

from typing import List, Union


def numeros_al_final_basico(lista: List[Union[float, str]]) -> List[Union[float, str]]:  # noqa: E501
    """Toma una lista de enteros y strings y devuelve una lista con todos los
    elementos numéricos al final.

    Restricciones:
        - Utilizar un bucle FOR.
        - Utilizar la función type.
        - No utilizar índices.
    """

    lista_enteros = []
    lista_no_enteros = []
    lista_compleata = []

    for i in lista:
        if type(i) == int:
            lista_enteros.append(i)
        else:
            lista_no_enteros.append(i)
    lista_compleata.extend(lista_no_enteros)
    lista_compleata.extend(lista_enteros)
    print("EJERCICIO N1:",lista_compleata) #MOSTRAMOS
    return lista_compleata

# NO MODIFICAR - INICIO
assert numeros_al_final_basico([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]  # noqa: E501
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_comprension(lista: List[Union[float, str]]) -> List[Union[float, str]]:  # noqa: E501
    """Re-escribir utilizando comprensión de listas.

    Restricciones:
        - No utilizar bucles.
        - Utilizar dos comprensiones de listas.
    """

    lista_no_enteros = ["a", "b", "j"] 
    lista_enteros = [3, 1, 10]

    lista_completa = [i for i in lista_no_enteros] + [i for i in lista_enteros]
    print("EJERCICIO N2:",lista_completa) #MOSTRAMOS
    return lista_completa
# NO MODIFICAR - INICIO
assert numeros_al_final_comprension([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]  # noqa: E501

#IMPRIMIMOS

# NO MODIFICAR - FIN
