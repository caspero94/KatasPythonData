"""
38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada
por el usuario.
"""

from datetime import datetime, time


def determinar_hora(hora: time) -> str:
    """Comprobamos en que rango esta la hora y retornamos"""
    hora_fix = hora.strftime("%H:%M")
    if hora >= time(6) and hora <= time(13):
        return f"Son las {hora_fix} y es por la mañana"
    elif hora <= time(21) and hora > time(13):
        return f"Son las {hora_fix} y es por la tarde"
    else:
        return f"Son las {hora_fix} y es de noche"


# Ejemplo
hora_actual = datetime.now().time()
print(determinar_hora(hora_actual))

# Ejemplo probar todas las horas del dia.
for x in range(0, 24):
    for y in range(0, 60, 15):
        print(determinar_hora(time(x, y)))
