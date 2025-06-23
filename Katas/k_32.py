"""
32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo
en la lista y devuelve el puesto del empleado si está en la lista, de lo contrario,
devuelve un mensaje indicando que la persona no trabaja aquí.
"""


def buscar_empleado(empleados: dict) -> str:
    """Acedemos a la lista de empleados y devolvemos su puesto, sino devolvemos un mensaje"""
    empleado = input("Ingrese el nombre del empleado: ").capitalize()
    try:
        print(f"El puesto de {empleado} es {empleados[empleado]}")
    except KeyError:
        print(f"La persona {empleado} no trabaja aqui.")


# Ejemplo
lista_empleados = {"Pedro": "Director", "Juan": "Carpitero", "Lucia": "Marketing"}
buscar_empleado(lista_empleados)
