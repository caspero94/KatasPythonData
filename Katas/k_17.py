"""
17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente.
Por ejemplo, [5,7,2] corresponde al número quinientos setenta y dos (572). Usa la función reduce()
"""

from functools import reduce


def lista_numero(digitos: list) -> int:
    """Acumulamos el primer numero x10 + el segundo, y asi sucesivamente"""
    return reduce(lambda x, y: x * 10 + y, digitos)


# Ejemplo
print(lista_numero([5, 7, 2, 7]))
