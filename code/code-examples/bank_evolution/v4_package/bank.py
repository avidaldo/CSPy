"""
Versión 4: Paquete
==================
Las validaciones están organizadas en un paquete con submódulos.
Esta es la estructura más profesional y escalable.

Estructura:
validators/
    __init__.py      (exporta las funciones principales)
    iban.py          (validaciones específicas de IBAN)
    amount.py        (validaciones de cantidades)

Mejoras respecto a v3:
- Mejor organización: cada tipo de validación en su propio módulo
- Más escalable: fácil añadir nuevos tipos de validación
- Aplicación del principio SRP (Single Responsibility Principle)
- Importaciones limpias gracias a __init__.py
"""
from validators import validate_iban, validate_positive_amount

# ====================
# EXCEPCIONES
# ====================


class InsufficientFundsError(Exception):
    """Se lanza cuando no hay fondos suficientes para una operación."""
    pass


# ====================
# CLASE PRINCIPAL
# ====================


class BankAccount:
    """
    Cuenta bancaria identificada por IBAN.
    
    Versión con paquete: usa un paquete estructurado para validaciones.
    Esta es la arquitectura más limpia y profesional.
    """

    def __init__(self, iban, initial_balance=0):
        """
        Crea una nueva cuenta bancaria.
        
        Args:
            iban: IBAN español válido (con checksum correcto)
            initial_balance: Saldo inicial (por defecto 0)
        """
        if not validate_iban(iban):
            raise ValueError(f"IBAN inválido: {iban}")

        if initial_balance < 0:
            raise ValueError("El saldo inicial no puede ser negativo")

        self._iban = iban
        self._balance = initial_balance

    @property
    def iban(self):
        """Devuelve el IBAN de la cuenta."""
        return self._iban

    @property
    def balance(self):
        """Devuelve el saldo actual."""
        return self._balance

    def deposit(self, amount):
        """Ingresa dinero en la cuenta."""
        if not validate_positive_amount(amount):
            raise ValueError("La cantidad debe ser positiva")

        self._balance += amount
        print(f"Ingreso: {amount:.2f}€. Nuevo saldo: {self._balance:.2f}€")

    def withdraw(self, amount):
        """Retira dinero de la cuenta."""
        if not validate_positive_amount(amount):
            raise ValueError("La cantidad debe ser positiva")

        if amount > self._balance:
            raise InsufficientFundsError(
                f"Fondos insuficientes. Saldo: {self._balance:.2f}€, "
                f"Intento de retirada: {amount:.2f}€")

        self._balance -= amount
        print(f"Retirada: {amount:.2f}€. Nuevo saldo: {self._balance:.2f}€")

    def transfer(self, target_account, amount):
        """Transfiere dinero a otra cuenta."""
        if not isinstance(target_account, BankAccount):
            raise TypeError("La cuenta destino debe ser un BankAccount")

        self.withdraw(amount)
        target_account.deposit(amount)
        print(f"Transferencia de {amount:.2f}€ a {target_account.iban}")

    def show(self):
        """Muestra la información de la cuenta."""
        print(f"IBAN: {self._iban}")
        print(f"Saldo: {self._balance:.2f}€")


# ====================
# EJEMPLO DE USO
# ====================

if __name__ == "__main__":
    print("=== Versión 4: Paquete ===\n")

    # IBANs válidos de prueba
    account1 = BankAccount("ES9121000418450200051332", 1000)
    account2 = BankAccount("ES7921000813610123456789", 500)

    print("Cuenta 1:")
    account1.show()
    print()

    print("Cuenta 2:")
    account2.show()
    print()

    # Operaciones
    print("--- Operaciones ---")
    account1.deposit(200)
    account1.withdraw(150)
    account1.transfer(account2, 100)
    print()

    print("--- Estado final ---")
    print("Cuenta 1:")
    account1.show()
    print()
    print("Cuenta 2:")
    account2.show()
    print()

    # Pruebas de validación
    print("--- Validación ---")

    try:
        invalid = BankAccount("ES1234567890123456789012", 100)
    except ValueError as e:
        print(f"✓ Detectado IBAN con checksum incorrecto: {e}")

    try:
        account1.withdraw(10000)
    except InsufficientFundsError as e:
        print(f"✓ Control de fondos: {e}")

    print("\n--- Beneficios de esta arquitectura ---")
    print("✓ Código organizado en paquetes y módulos")
    print("✓ Cada módulo tiene una única responsabilidad (SRP)")
    print("✓ Separación clara de responsabilidades (SoC)")
    print("✓ Fácil de mantener, probar y extender")
    print("✓ El paquete 'validators' se puede reutilizar")
