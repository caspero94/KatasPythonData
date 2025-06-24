"""
39. Escribe un programa que determine qué calificación en texto tiene
un alumno en base a su calificación numérica.
Las reglas de calificación son:
- 0 - 69 insuficiente
- 70 - 79 bien
- 80 - 89 muy bien
- 90 - 100 excelente
"""


def determinar_calificacion(nota: int) -> str:
    """Comprobamos nota y asignamos"""
    if nota in range(0, 70):
        return f"{nota} : Insuficiente"
    elif nota in range(70, 80):
        return f"{nota} : Bien"
    elif nota in range(80, 90):
        return f"{nota} : Muy Bien"
    elif nota in range(90, 101):
        return f"{nota} : Excelente"
    else:
        return f"{nota} : Nota sin calificacion correspondiente"


# Ejemplo probando desde -1 a 101
for x in range(-1, 102):
    print(determinar_calificacion(x))
