"""
2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()
"""

# Ejemplo
numeros = [1, 2, 3, 4, 5, 6]

# Aplicar map con funcion lamda que multiplique *2 y el array de numeros y envolver en una lista
numeros_doble = list(map(lambda n: n * 2, numeros))

# Ejecución
print(numeros_doble)
