"""
34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos.
Los métodos disponibles son: crecer_tronco, nueva_rama, crecer_ramas, quitar_rama e info_arbol.
El objetivo es implementar estos métodos para manipular la estructura del árbol.

Código a seguir:

1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas
las ramas existentes.
5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
6. Implementar el método info_arbol para devolver información sobre la longitud del tronco,
el número de ramas y las longitudes de las mismas.

Caso de uso:

1. Crear un árbol.
2. Hacer crecer el tronco del árbol una unidad.
3. Añadir una nueva rama al árbol.
4. Hacer crecer todas las ramas del árbol una unidad.
5. Añadir dos nuevas ramas al árbol.
6. Retirar la rama situada en la posición 2.
7. Obtener información sobre el árbol.
"""


class Arbol:
    """Arbol con tronco y ramas"""

    def __init__(self) -> None:
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self) -> print:
        """Aumenta el tronco"""
        self.tronco += 1
        return print(f"Crecio el tronco, tamaño {self.tronco}")

    def nueva_rama(self) -> print:
        """Agrega una rama"""
        self.ramas.append(1)
        return print(f"Crecio una rama, tenemos {len(self.ramas)}")

    def crecer_ramas(self) -> print:
        """Crecen las ramas"""
        for i, _ in enumerate(self.ramas):
            self.ramas[i] += 1
        print(f"Crecieron las ramas, logitudes de ramas: {self.ramas}")

    def quitar_rama(self, posicion) -> print:
        """Quita una rama"""
        del self.ramas[posicion]
        return print(f"Se quito la rama en posicion {posicion}, tenemos {self.ramas}")

    def info_arbol(self) -> print:
        """Devuelve informacion del tronco y ramas"""
        return print(
            f"Tronco: {self.tronco}, Ramas: {len(self.ramas)} longitudes: {self.ramas}"
        )


arbol = Arbol()
arbol.crecer_tronco()
arbol.nueva_rama()
arbol.crecer_ramas()
arbol.nueva_rama()
arbol.nueva_rama()
arbol.quitar_rama(2)
arbol.info_arbol()
