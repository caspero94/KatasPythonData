"""
18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de
estudiantes (nombre, edad, calificación) y use la función filter para extraer a los estudiantes
con una calificación mayor o igual a 90. Usa la función filter()
"""

from random import randint


class DataEstudiante:
    """Base de datos de estudiantes"""

    def __init__(self):
        self.database = []

    def agregar_estudiante(self, nombre: str, edad: int, calificacion: int) -> None:
        """Funcion para agregar estudiantes a la data"""
        self.database.append(
            {"nombre": nombre, "edad": edad, "calificacion": calificacion}
        )

    def filtar_estudiantes(self) -> list[dict[str, int | str]]:
        """Filtamos los estudiantes > 90 en clasificacion"""
        return list(filter(lambda x: x["calificacion"] >= 90, self.database))


# Ejemplo
ejemplo_estudiantes = ["Pedro", "Paco", "Juan", "Elisa", "Pepa", "Jorge", "Veronica"]
estudiantes = DataEstudiante()

# Agremamos estudiantes con datos aleatorios
for estudiante in ejemplo_estudiantes:
    estudiantes.agregar_estudiante(estudiante, randint(10, 50), randint(80, 100))


print(f"BASE DE ESTUDIANTES {estudiantes.database}")
print(f"Estudiantes > 90: {estudiantes.filtar_estudiantes()}")
