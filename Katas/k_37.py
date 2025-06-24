"""
37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada:
contar_palabras, reemplazar_palabras, eliminar_palabra. Estas opciones son otras funciones
que tenemos que definir primero y llamar dentro de la función procesar_texto.

Código a seguir:

1. Crear una función contar_palabras para contar el número de veces que aparece cada
palabra en el texto. Tiene que devolver un diccionario.
2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una
palabra_nueva. Tiene que devolver el texto con el remplazo de palabras.
3. Crear una función eliminar_palabra para eliminar una palabra del texto.
Tiene que devolver el texto con la palabra eliminada.
4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar",
"eliminar") y un número de argumentos variable según la opción indicada.

Caso de uso:

Comprueba el funcionamiento completo de la función procesar_texto
"""

from functools import reduce


def procesar_texto(texto: str, opcion: str, *args) -> str | dict:
    """Funcion principal"""
    # No se explico swich(agregado 3.10)en master, es mas conveniente que if elif/diccionario metodo
    l_texto = texto.split()
    try:
        match opcion:
            case "contar":
                return contar_palabras(l_texto)
            case "reemplazar":
                return reemplazar_palabras(l_texto, args[0], args[1])
            case "eliminar":
                return eliminar_palabra(l_texto, args[0])
            case _:
                raise ValueError("Opción no valida.")

    except ValueError as e:
        print(f"ERROR: {e}")


def contar_palabras(texto: list) -> dict:
    """Funcion contar palabras"""
    # Enfoque For:
    # conteo = dict()
    # for palabra in texto:
    #     conteo[palabra] = conteo.get(palabra, 0) + 1
    # return conteo

    # Enfoque Reduce: aplicamos lambda acc (diccionario), pal (palabra actual), usamos el metodo
    # update para agregar/actualizar la palabra, con get para para asignar el conteo existente o 0
    # y sumarle 1, como update devuelve none aplicamos or acc, para devolver el diccionario
    return reduce(
        lambda acc, pal: acc.update({pal: acc.get(pal, 0) + 1}) or acc,
        texto,
        {},
    )


def reemplazar_palabras(texto: list, original: str, nueva: str) -> str:
    """Funcion reemplazar palabras"""
    # Enfoque For:
    # return " ".join([nueva if pal == original else pal for pal in texto])

    # Enfoque Map:
    return " ".join(map(lambda pal: nueva if pal == original else pal, texto))


def eliminar_palabra(texto: list, eliminar: str) -> str:
    """Funcion eliminar palabra"""
    # Enfoque For:
    # return " ".join([palabra for palabra in texto if palabra != eliminar])

    # Enfoque Filter:
    return " ".join(filter(lambda pal: pal != eliminar, texto))


# Ejemplos
TEXTO_EJEMPLO = """Crea una función llamada función que haga funciones jeje"""

palabras_contadas = procesar_texto(TEXTO_EJEMPLO, "contar")
print(palabras_contadas)

texto_reemplazado = procesar_texto(TEXTO_EJEMPLO, "reemplazar", "función", "canción")
print(texto_reemplazado)

texto_eliminado = procesar_texto(TEXTO_EJEMPLO, "eliminar", "función")
print(texto_eliminado)
