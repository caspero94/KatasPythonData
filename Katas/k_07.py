"""
7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()
"""


def convertir_tupla_string(tuplas: tuple) -> list:
    """Convertir tupla en string con map"""
    return list(map(str, tuplas))


# Ejemplo
ejemplo_tupla = ("Ana", 28, "hora", "horacio")
print(convertir_tupla_string(ejemplo_tupla))
