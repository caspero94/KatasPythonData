"""
1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con
las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.
"""


def frecuencia_letras(texto: str) -> dict:
    """Frecuencia de cada letra usando for e if para agregar o establecer la frecuencia"""
    frecuencia = {}
    for letra in texto:
        letra = letra.lower()
        if letra != " ":
            if letra in frecuencia:
                frecuencia[letra] += 1
            if letra not in frecuencia:
                frecuencia[letra] = 1
    return frecuencia


# Ejemplo
EJEMPLO = "Probando texto para que mida la frecuencia de cada letra"

print(frecuencia_letras(EJEMPLO))
