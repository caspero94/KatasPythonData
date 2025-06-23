"""
19. Crea una función lambda que filtre los números impares de una lista dada.
"""

lista_ejemplo = [2, 5, 43, 342, 21, 325, 64, 32, 234]

"""Funcion lambda que recibe una lista y filtra usando lambda para determinar impar"""
filtrar_impares = lambda lista: list(filter(lambda x: x % 2 != 0, lista))
print(filtrar_impares(lista_ejemplo))
