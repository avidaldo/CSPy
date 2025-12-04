import re


# Function to validate Spanish DNI
def validate_dni(dni: str) -> bool:
    """Validate a Spanish DNI (8 digits followed by a letter)."""
    pattern = r'^[0-9]{8}[A-Z]$'
    return bool(re.match(pattern, dni))


class BankAccount:
    """A simple bank account."""

    def __init__(self, dni: str, initial_balance: float = 0):
        """Initialize a new bank account."""
        if not validate_dni(dni):
            raise ValueError(
                "Invalid DNI format. Must be 8 digits followed by a letter.")
        self.dni = dni  # Attribute: DNI of the account holder
        self.balance = initial_balance  # Attribute: current balance

    def deposit(self, amount):
        """Add money to the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        """Remove money from the account."""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Insufficient funds or invalid amount.")

    def show(self):
        """Display account information."""
        print(f"Account DNI: {self.dni}")
        print(f"Balance: ${self.balance:.2f}")


# Example usage
alice_account = BankAccount("12345678A", 1000.0)
bob_account = BankAccount("87654321B", 500.0)

alice_account.show()
