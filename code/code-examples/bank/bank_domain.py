import re


class InsufficientFundsError(Exception):
    """Custom exception for insufficient funds."""
    pass


# Function to validate Spanish DNI
def validate_dni(dni: str) -> bool:
    """Validate a Spanish DNI (8 digits followed by a letter)."""
    pattern = r'^[0-9]{8}[A-Z]$'
    return bool(re.match(pattern, dni))


class BankAccount:
    """A simple bank account."""

    def __init__(self, dni: str, iban: str, initial_balance: float = 0):
        """Initialize a new bank account."""
        if not validate_dni(dni):
            raise ValueError(
                "Invalid DNI format. Must be 8 digits followed by a letter.")
        if not self._validate_iban(iban):
            raise ValueError(
                "Invalid IBAN format. Must be a valid Spanish IBAN (ES + 22 digits)."
            )
        self._dni = dni
        self._iban = iban
        self._balance = initial_balance

    @property
    def dni(self) -> str:
        return self._dni

    @property
    def iban(self) -> str:
        return self._iban

    @property
    def balance(self) -> float:
        return self._balance

    @staticmethod
    def _validate_iban(iban: str) -> bool:
        """Validate a Spanish IBAN (starts with 'ES', 24 characters, alphanumeric)."""
        pattern = r'^ES[0-9]{22}$'
        return bool(re.match(pattern, iban))

    def deposit(self, amount: float):
        """Add money to the account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount

    def withdraw(self, amount: float):
        """Remove money from the account."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise InsufficientFundsError("Insufficient funds.")
        self._balance -= amount

    def __str__(self):
        """Return account information as a string."""
        return (f"Account DNI: {self._dni}\n"
                f"IBAN: {self._iban}\n"
                f"Balance: ${self._balance:.2f}")


# Example usage
if __name__ == "__main__":
    # Basic testing
    print("Running basic tests...")
    test_account = BankAccount("12345678A", "ES7620770024003102575766", 100.0)
    assert test_account.balance == 100.0

    test_account.deposit(50.0)
    assert test_account.balance == 150.0

    test_account.withdraw(20.0)
    assert test_account.balance == 130.0

    try:
        test_account.withdraw(1000.0)
        print("Test failed: Should have raised InsufficientFundsError")
        exit()
    except InsufficientFundsError:
        pass # Expected

    print("All basic tests passed.")
