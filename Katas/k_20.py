"""
20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los
valores int. Usa la función filter()
"""


def filtro_int(lista: list) -> list[int]:
    """Filtramos int de str y tambien str que son digitos, luego aplicamos un map para
    convetir los str numericos a int y retornamos"""
    return list(
        map(int, list(filter(lambda x: isinstance(x, int) or x.isdigit(), lista)))
    )


# Ejemplo
lista_ejemplo = [23, "34", "golmas", 32, "dw", "3432"]
print(filtro_int(lista_ejemplo))
