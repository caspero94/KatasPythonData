"""
23. Concatena una lista de palabras.Usa la función reduce().
"""

from functools import reduce


def concatena(n: list[str]) -> str:
    """Concatenamos el string total sumando el string y un espacio blanco"""
    return reduce(lambda x, y: x + " " + y, n)


# Ejemplo
lista_ejemplo = ["Hola", "mundo", "Python", "es", "lo", "mejor"]
print(concatena(lista_ejemplo))
