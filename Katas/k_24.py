"""
24. Calcula la diferencia total en los valores de una lista. Usa la función reduce().
"""

from functools import reduce


def diferencia_total(n: list[int]) -> int:
    """Calcula diferencia restando acumulado"""
    return reduce(lambda x, y: x - y, n)


# Ejemplo
lista_ejemplo = [59, 23, 12, 3, 20]
print(diferencia_total(lista_ejemplo))
