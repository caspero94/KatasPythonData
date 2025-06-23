"""
27. Crea una función que calcule el promedio de una lista de números
"""


def promedio(numeros: list) -> float:
    """Calcula promedio"""
    return sum(numeros) / len(numeros)


# Ejemplo
lista_ejemplo = [1, 2, 5, 8, 25]
print(promedio(lista_ejemplo))
