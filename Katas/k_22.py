"""
22. Dada una lista numérica, obtén el producto total de los valores
de dicha lista.Usa la función reduce().
"""

from functools import reduce


def total(n: list[int]) -> int:
    """Calcula el total sumando el acumulado"""
    return reduce(lambda x, y: x + y, n)


# Ejemplo
lista_ejemplo = [5, 5, 8, 23, 12, 3, 20, 50]
print(total(lista_ejemplo))
