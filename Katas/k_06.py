"""
6. Escribe una función que calcule el factorial de un número de manera recursiva.
"""


def calcular_factorial(n: int) -> int:
    """Factorial recursivo caso base n-1 y salida n=1"""
    if n < 0:
        raise ValueError("Factorial definido para numeros enteros no negativos")
    return 1 if n in (0, 1) else n * calcular_factorial(n - 1)


# Ejemplo
print(calcular_factorial(1))
