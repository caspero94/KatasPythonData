"""
30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por
las mismas letras pero en diferente orden.
"""


def compara_anagramas(ana1: str, ana2: str) -> bool:
    """Ordenamos las letras en minusculas y si coincide, esta correcto"""
    return sorted(ana1.lower().strip()) == sorted(ana2.lower().strip())


# Ejemplo
ANAGRAMA1 = "Perro "
ANAGRAMA2 = "ReprO"

print(compara_anagramas(ANAGRAMA1, ANAGRAMA2))
