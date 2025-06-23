"""
28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
"""


def buscar_duplicado(lista: list):
    """Buscar primer duplicado, agrega a una lista temporal los elementos recorridos
    hasta encontrar uno que ya este en la temp"""
    lista_temp = []
    for elemento in lista:
        if elemento not in lista_temp:
            lista_temp.append(elemento)
        else:
            return elemento


# Ejemplo
lista_ejemplo = [10, 20, 25, 15, 20, 10]
print(buscar_duplicado(lista_ejemplo))
