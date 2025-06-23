"""
16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva
una lista de todas las palabras que sean más largas que n. Usa la función filter()
"""


def filtro_len_n(texto: str, n: int) -> list:
    """Funcion filtra palabras > n"""
    return list(filter(lambda t: len(t) > n, texto.split()))


TEXTO_EJEMPLO = """Escribe una función que tome una cadena de texto y un número entero n como
parámetros y devuelva una lista de todas las palabras que sean más largas que n."""
print(filtro_len_n(TEXTO_EJEMPLO, 6))
