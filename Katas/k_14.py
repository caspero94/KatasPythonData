"""
14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en
especifico. Usa la función filter()
"""


def filtrar_palarbas(palabras: list, letra: str) -> list:
    """Aplicamos filtro con lower para que retorne tanto minus/mayus, usamos startswith
    para evitar error de indice en strings vacios f[0] == letra"""

    return list(filter(lambda f: f.lower().startswith(letra.lower()), palabras))


lista_palabras_ejemplo = ["HOLA", "CALOR", "VERANO", "AZUL", "cAiMan", "Clima", ""]
print(filtrar_palarbas(lista_palabras_ejemplo, "c"))
