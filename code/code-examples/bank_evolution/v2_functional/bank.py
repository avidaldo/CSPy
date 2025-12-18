"""
Versión 2: Funcional
====================
La validación se extrae a funciones independientes.
Esto mejora la Separación de Responsabilidades (SoC).

Mejoras respecto a v1:
- Las funciones de validación pueden reutilizarse
- La clase BankAccount es más simple y enfocada
- Es más fácil probar las validaciones
"""
import re

# ====================
# FUNCIONES DE VALIDACIÓN
# ====================


def validate_iban_format(iban):
    """
    Valida el formato de un IBAN español.
    
    Args:
        iban: String con el IBAN a validar
    
    Returns:
        bool: True si el formato es correcto
    """
    pattern = r'^ES\d{22}$'
    return bool(re.match(pattern, iban))


def validate_positive_amount(amount):
    """
    Valida que una cantidad sea positiva.
    
    Args:
        amount: Cantidad a validar
    
    Returns:
        bool: True si es positiva
    """
    return amount > 0


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
    
    Versión funcional: usa funciones externas para validación.
    La clase se enfoca solo en la lógica de cuenta bancaria.
    """

    def __init__(self, iban, initial_balance=0):
        """
        Crea una nueva cuenta bancaria.
        
        Args:
            iban: IBAN español (ES + 22 dígitos)
            initial_balance: Saldo inicial (por defecto 0)
        """
        # Usa las funciones de validación externas
        if not validate_iban_format(iban):
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
    print("=== Versión 2: Funcional ===\n")

    # Crear cuentas
    account1 = BankAccount("ES1234567890123456789012", 1000)
    account2 = BankAccount("ES9876543210987654321098", 500)

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

    # Ahora podemos probar las funciones directamente
    assert validate_iban_format("ES1234567890123456789012") == True
    assert validate_iban_format("ES123") == False
    assert validate_positive_amount(100) == True
    assert validate_positive_amount(-50) == False
    print("✓ Todas las validaciones pasaron")

    try:
        invalid = BankAccount("ES123", 100)
    except ValueError as e:
        print(f"✓ Validación IBAN: {e}")

    try:
        account1.withdraw(10000)
    except InsufficientFundsError as e:
        print(f"✓ Control de fondos: {e}")
