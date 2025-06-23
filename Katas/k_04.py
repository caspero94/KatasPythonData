"""
4. Genera una función que calcule la diferencia entre los valores de dos listas.Usa la función map()
"""


def calcular_diferencia(lista1: list, lista2: list) -> list:
    """Calculamos la diferencia con map y funcion lambda"""
    return list(map(lambda x, y: x - y, lista1, lista2))


# Ejemplo
ejemplo1 = [10, 20, 30, 10]
ejemplo2 = [5, 15, 25, 50]
resultado = calcular_diferencia(ejemplo1, ejemplo2)
print(resultado)
