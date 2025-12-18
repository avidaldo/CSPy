"""
Versión 1: Monolítica
=====================
Todo el código está en una clase. La validación de IBAN está dentro de la clase.
Esto funciona para empezar, pero tiene problemas de organización.
"""
import re


class InsufficientFundsError(Exception):
    """Se lanza cuando no hay fondos suficientes para una operación."""
    pass


class BankAccount:
    """
    Cuenta bancaria identificada por IBAN.
    
    Versión monolítica: toda la lógica está dentro de la clase,
    incluyendo la validación de IBAN.
    """

    def __init__(self, iban, initial_balance=0):
        """
        Crea una nueva cuenta bancaria.
        
        Args:
            iban: IBAN español (ES + 22 dígitos)
            initial_balance: Saldo inicial (por defecto 0)
        """
        # Validación inline - todo está dentro de la clase
        if not self._is_valid_iban(iban):
            raise ValueError(f"IBAN inválido: {iban}")

        if initial_balance < 0:
            raise ValueError("El saldo inicial no puede ser negativo")

        self._iban = iban
        self._balance = initial_balance

    def _is_valid_iban(self, iban):
        """
        Valida un IBAN español (formato básico).
        Versión simple: solo comprueba el formato con regex.
        """
        # Solo formato: ES + 22 dígitos
        pattern = r'^ES\d{22}$'
        return bool(re.match(pattern, iban))

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
        if amount <= 0:
            raise ValueError("La cantidad debe ser positiva")

        self._balance += amount
        print(f"Ingreso: {amount:.2f}€. Nuevo saldo: {self._balance:.2f}€")

    def withdraw(self, amount):
        """Retira dinero de la cuenta."""
        if amount <= 0:
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

        # Retirar de esta cuenta
        self.withdraw(amount)
        # Ingresar en la cuenta destino
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
    print("=== Versión 1: Monolítica ===\n")

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

    # Pruebas de validación (usando asserts como en los notebooks de módulos)
    print("--- Validación ---")
    try:
        invalid = BankAccount("ES123", 100)  # IBAN incorrecto
    except ValueError as e:
        print(f"✓ Validación correcta: {e}")

    try:
        account1.withdraw(10000)  # Fondos insuficientes
    except InsufficientFundsError as e:
        print(f"✓ Control de fondos correcto: {e}")
