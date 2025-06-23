"""
29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los
caracteres  con el carácter '#', excepto los últimos cuatro.
"""


def ocultar(text: object) -> str:
    """Tomamos la longitud menos 4 y la multiplicamos por # y agregamos las ultimas 4"""
    return "#" * len(str(text)[:-4]) + str(text)[-4:]


# Ejemplo
VARIABLE = 14541.5076463
print(ocultar(VARIABLE))
