"""
13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con
cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map()
"""


def letras_mayus_minus(ca: str) -> list:
    """Convetimos a minus, filtramos letras, aplicamos set y map para generar mayus/minus"""

    return list(
        map(lambda c: (c.upper(), c.lower()), set(filter(str.isalpha, ca.lower())))
    )


# Ejemplo
EJEMPLO = "AaBcDfF, 3223; zdw"
print(letras_mayus_minus(EJEMPLO))
