"""
11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor
no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120,
maneja las excepciones adecuadamente.
"""


class FueraDeRango(Exception):
    """Creamos excepcion para valores fuera de rango"""


def control_edad() -> None:
    """Solicitamos edad y manejamos error de tipo dato y de rango"""
    while True:
        try:
            edad = int(input("Ingrese su edad por favor: "))
            if edad < 1 or edad > 120:
                raise FueraDeRango(
                    "Edad fuera de rango, ingrese una edad entre 1 y 120"
                )
            print(f"Edad válida registrada: {edad} años")
            break
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")

        except FueraDeRango as e:
            print(f"Error: {e}")


# Ejecución
control_edad()
