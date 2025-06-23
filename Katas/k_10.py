"""
10. Escribe una función que reciba una lista de números y calcule su promedio.
Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.
"""


class ListaVaciaError(Exception):
    """Creamos la excepcion para listas vacias"""


def calcular_promedio(lista_numeros: list) -> float:
    """Comprobamos si la lista esta vacias y devolvemos el promedio u error"""
    if not lista_numeros:
        raise ListaVaciaError("La lista esta vacia")
    return sum(lista_numeros) / len(lista_numeros)


# Ejemplo, capturando error en tiempo de ejecucción
try:
    print(f"El promedio es: {calcular_promedio([15, 54, 215])}")
    print(f"El promedio es: {calcular_promedio([])}")
except ListaVaciaError as e:
    print(f"Error: {e}")
