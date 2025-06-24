"""
40. Escribe una función que tome dos parámetros:
figura (una cadena que puede ser "rectangulo" , "circulo" o "triangulo") y
datos (una tupla con los datos necesarios para calcular el área de la figura).
"""

import math


def area(figura: str, *arg: tuple[int]) -> float | int:
    """Determinamos que figura es y calculamos el area si la figura no se encuentra envia error"""
    try:
        match figura:
            case "circulo":
                return math.pi * arg[0] ** 2

            case "triangulo":
                return (arg[0] * arg[1]) / 2

            case "rectangulo":
                return arg[0] * arg[1]

            case _:
                raise ValueError("Figura no encontrada")

    except ValueError as e:
        return f"ERROR: {e}"


print(area("circulo", 5))
print(area("triangulo", 5, 10))
print(area("rectangulo", 5, 10))
print(area("rombo", 25))
