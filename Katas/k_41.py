"""
41. En este ejercicio, se pedirá que escribas un programa en Python que utilice condicionales para
determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento.
El programa debe hacer lo siguiente:
1. Solicita al usuario que ingrese el precio original de un artículo.
2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea
válido(es decir, mayor a cero). Por ejemplo, descuento de 15€.
5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo
estas acciones en tu programa de Python.
"""


def monto_final() -> float | str:
    """Calcular precio final y controlamos errores"""
    try:
        precio_original = float(input("Ingrese precio original: "))
        descuento = 0
        if input("Tienes descuento? (si/no): ").strip().lower() == "si":
            descuento = float(input("Ingrese el valor del descuento: "))
            if descuento <= 0:
                raise ValueError("Descuento no es valido.")

        return round(precio_original - descuento, 2)

    except ValueError as e:
        return f"Error: {e}"


# Ejemplo
print(monto_final())
