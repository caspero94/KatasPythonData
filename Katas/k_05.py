"""
5. Ecribe una función que tome una lista de números como parámetro y un valor opcional
nota_aprobado, que por defecto es 5. La función debe calcular la media de los números en la lista y
determinar si la media es mayor o igual que nota aprobado. Si es así, el estado será "aprobado", de
lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado.
"""


def aprueba(lista_numeros: list, aprobado: int = 5) -> tuple:
    """Sumamos lista de numeros y dividimos entre la cantidad de elementos y aplica condicional"""
    if not lista_numeros:
        return (0, "Suspenso")
    media = sum(lista_numeros) / len(lista_numeros)
    estado = "Aprobado" if media >= aprobado else "Suspenso"
    return (media, estado)


# Ejemplo
ejemplo_notas = [5, 5, 9, 2, 6, 8, 1, 3, 4]
EJEMPLO_APROBADO = 3
print(aprueba(ejemplo_notas, EJEMPLO_APROBADO))
