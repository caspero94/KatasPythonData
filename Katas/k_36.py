"""
36. Crea la clase UsuarioBanco, representa a un usuario de un banco con su nombre, saldo y si
tiene o no cuenta corriente. Proporciona métodos para realizar operaciones como retirar dinero,
transferir dinero desde otro usuario y agregar dinero al saldo.

Código a seguir:

1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente
mediante True y False.
2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario.
Lanzará un error en caso de no poder hacerse.
3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario
al usuario actual. Lanzará un error en caso de no poder hacerse.
4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.

Caso de uso:

1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50,
ambos con cuenta corriente.
2. Agregar 20 unidades de saldo de "Bob".
3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
4. Retirar 50 unidades de saldo a "Alicia".
"""


class UsuarioBanco:
    """Definimos las propiedades y metodos del UsuarioBanco"""

    def __init__(self, nombre: str, saldo: int, cuenta_corriente: bool):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad: int) -> str:
        """Retirar dinero de la cuenta"""
        if self.saldo < cantidad:
            raise ValueError("Saldo insuficiente en la cuenta para realizar retiro.")
        self.saldo -= cantidad
        return f"{self.nombre} retiro {cantidad} de la cuenta."

    def agregar_dinero(self, cantidad: int) -> str:
        """Agregar dinero a la cuenta"""
        self.saldo += cantidad
        return f"{self.nombre} ingreso {cantidad} en la cuenta."

    def transferir_dinero(self, cantidad: int, usuario: object) -> str:
        """Trasferir dinero de un usuario a otro"""
        if self.saldo < cantidad:
            raise ValueError(
                f"Saldo insuficiente en la cuenta de {self.nombre} para realizar transferencia."
            )
        self.retirar_dinero(cantidad)
        usuario.agregar_dinero(cantidad)
        return f"{self.nombre} transfirio {cantidad} a {usuario.nombre}"


alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)
print(bob.agregar_dinero(20))
try:
    print(bob.transferir_dinero(80, alicia))
except ValueError as e:
    print(f"Error: {e}")
try:
    print(alicia.retirar_dinero(50))
except ValueError as e:
    print(f"Error: {e}")


print(alicia.__dict__)
print(bob.__dict__)
