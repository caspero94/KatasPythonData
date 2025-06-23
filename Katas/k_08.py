"""
8. Escribe un programa que pida al usuario dos números e intente dividirlos.
Si el usuario ingresa un valor no numérico o intenta dividir por cero,
maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
indicando si la división fue exitosa o no.
"""


def dividir_numeros():
    """Dividir 2 numeros y controlar errores"""
    while True:
        try:
            print("-- DIVISION --")
            n1 = int(input("Ingrese primer numero: "))
            n2 = int(input("Ingrese segundo numero: "))
            print(f"División exitosa, resultado: {n1/n2}")
            break
        except ValueError:
            print("Por favor ingrese un numero, texto no valido")

        except ZeroDivisionError:
            print("No se puede divivir por cero")


# Ejecuccion
dividir_numeros()
