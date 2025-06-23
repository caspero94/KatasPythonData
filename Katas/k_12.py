"""
12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra.
Usa la función map()
"""


def longitud_palabras_frase(frase: str) -> list:
    """Split a la frase para separarla en palabras y map con len para retornar lista longitud"""
    return list(map(len, frase.split()))


# Ejemplo
EJEMPLO = "HOLA MUNDO PITAGORAS"
print(longitud_palabras_frase(EJEMPLO))
