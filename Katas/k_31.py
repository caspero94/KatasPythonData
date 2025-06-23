"""
31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un
nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando
que fue encontrado, de lo contrario, se lanza una excepción.
"""


def buscar_nombre() -> str:
    """Invocamos generar nombres, y solicitamos nombre a buscar y comprobamos"""
    nombres_input = input("Introduce nombres separados por comas: ")
    nombres = [nombre.strip() for nombre in nombres_input.split(",")]
    nombre = input("Nombre a buscar: ")
    if nombre not in nombres:
        raise ValueError(f"Nombre {nombre} no encontrado.")
    return f"El nombre {nombre} fue encontrado."


# Ejemplo
try:
    print(buscar_nombre())
except ValueError as e:
    print(f"Error: {e}")
