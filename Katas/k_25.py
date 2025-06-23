"""
25. Crea una función que cuente el número de caracteres en una cadena de texto dada.
"""


def contar_caracteres(texto: str) -> int:
    """Quitamos espacios y calculamos longitud"""
    return len(texto.replace(" ", ""))


# Ejemplo
print(contar_caracteres("Pedro pica piedra"))
