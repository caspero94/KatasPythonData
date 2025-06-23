"""
9. Escribe una función que tome una lista de nombres de mascotas como parámetro
y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España.
La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"].
Usa la función filter()
"""


def excluir_mascotas(lista_mascotas: list) -> list:
    """Filtrar mascotas prohibidas y devolver la lista"""
    lista_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]

    return list(filter(lambda mascota: mascota not in lista_prohibidas, lista_mascotas))


# Ejemplo
mascotas_ejeplo = ["Perro", "Tigre", "Oveja", "Cocodrilo", "Gato"]
print(excluir_mascotas(mascotas_ejeplo))
