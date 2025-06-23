"""
15. Crea una función lambda que sume 3 a cada número de una lista dada.
"""


def suma_3(numeros: list) -> list:
    """Sumamos 3 a cada numero de la lista"""
    return list(map(lambda x: x + 3, numeros))


# Ejemplo
lista_ejemeplo = [1, 5, 3, 8]
print(suma_3(lista_ejemeplo))
