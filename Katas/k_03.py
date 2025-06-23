"""
3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros.
La función debe devolver una lista con todas las palabras de la lista original
que contengan la palabra objetivo.
"""


def metodo_for(lista: list, objetivo: str) -> list:
    """METODO FOR"""
    resultado = []
    for palabra in lista:
        if objetivo.lower() in palabra.lower():
            resultado.append(palabra)

    return resultado


def metodo_filter(lista: list, objetivo: str) -> list:
    """METODO FILTER"""
    return list(filter(lambda n: objetivo.lower() in n.lower(), lista))


# Ejemplo
ejemplo_lista = [
    "programar",
    "accionaR",
    "dibujante",
    "amargo",
    "dulce",
    "memorizar",
    "ELEaRLl",
]
EJEMPLO_OBJETIVO = "ar"

print(metodo_for(ejemplo_lista, EJEMPLO_OBJETIVO))
print(metodo_filter(ejemplo_lista, EJEMPLO_OBJETIVO))
