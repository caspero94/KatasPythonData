"""
33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.
"""

# Ejemplo
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

# Funcion lambda que suma los elementos de cada lista en 1
sumar_elementos = list(map(lambda x, y: x + y, lista1, lista2))
print(sumar_elementos)
