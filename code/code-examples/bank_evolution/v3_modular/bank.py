"""
Versión 3: Modular
==================
La validación está en un módulo separado (validators.py).
Ahora incluye validación completa de IBAN con checksum MOD-97.

Mejoras respecto a v2:
- Mejor organización: validaciones en su propio módulo
- Validación completa de IBAN (no solo formato)
- El módulo validators se puede reutilizar en otros proyectos
- Aplicación del principio DRY (Don't Repeat Yourself)
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
    
    Versión modular: usa un módulo externo para validaciones.
    La validación de IBAN ahora incluye verificación de checksum.
    """

    def __init__(self, iban, initial_balance=0):
        """
        Crea una nueva cuenta bancaria.
        
        Args:
            iban: IBAN español válido (con checksum correcto)
            initial_balance: Saldo inicial (por defecto 0)
        """
        # Validación completa de IBAN (formato + checksum)
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
    print("=== Versión 3: Modular ===\n")

    # Ahora usamos IBANs válidos (con checksum correcto)
    # Puedes generar IBANs de prueba en: https://www.generateiban.com/
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

    # IBAN con formato correcto pero checksum incorrecto
    try:
        invalid = BankAccount("ES1234567890123456789012", 100)
    except ValueError as e:
        print(f"✓ Detectado IBAN con checksum incorrecto: {e}")

    # IBAN con formato incorrecto
    try:
        invalid2 = BankAccount("ES123", 100)
    except ValueError as e:
        print(f"✓ Detectado IBAN con formato incorrecto: {e}")

    # Fondos insuficientes
    try:
        account1.withdraw(10000)
    except InsufficientFundsError as e:
        print(f"✓ Control de fondos: {e}")
