"""
Version 3: Modular
==================
Validation is in a separate module (validators.py).
Now includes full IBAN validation with MOD-97 checksum.

Improvements over v2:
- Better organization: validations in their own module
- Full IBAN validation (not just format)
- The validators module can be reused in other projects
- DRY (Don't Repeat Yourself) principle application
"""
from validators import validate_iban, validate_positive_amount

# ====================
# EXCEPTIONS
# ====================


class InsufficientFundsError(Exception):
    """Raised when there are insufficient funds for an operation."""
    pass


# ====================
# MAIN CLASS
# ====================


class BankAccount:
    """
    Bank account identified by IBAN.
    
    Modular version: uses an external module for validations.
    IBAN validation now includes checksum verification.
    """

    def __init__(self, iban, initial_balance=0):
        """
        Creates a new bank account.
        
        Args:
            iban: Valid Spanish IBAN (with correct checksum)
            initial_balance: Initial balance (default 0)
        """
        # Full IBAN validation (format + checksum)
        if not validate_iban(iban):
            raise ValueError(f"Invalid IBAN: {iban}")

        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")

        self._iban = iban
        self._balance = initial_balance

    @property
    def iban(self):
        """Returns the account's IBAN."""
        return self._iban

    @property
    def balance(self):
        """Returns the current balance."""
        return self._balance

    def deposit(self, amount):
        """Deposits money into the account."""
        if not validate_positive_amount(amount):
            raise ValueError("Amount must be positive")

        self._balance += amount
        print(f"Deposit: {amount:.2f}€. New balance: {self._balance:.2f}€")

    def withdraw(self, amount):
        """Withdraws money from the account."""
        if not validate_positive_amount(amount):
            raise ValueError("Amount must be positive")

        if amount > self._balance:
            raise InsufficientFundsError(
                f"Insufficient funds. Balance: {self._balance:.2f}€, "
                f"Withdrawal attempt: {amount:.2f}€")

        self._balance -= amount
        print(f"Withdrawal: {amount:.2f}€. New balance: {self._balance:.2f}€")

    def transfer(self, target_account, amount):
        """Transfers money to another account."""
        if not isinstance(target_account, BankAccount):
            raise TypeError("Target account must be a BankAccount")

        self.withdraw(amount)
        target_account.deposit(amount)
        print(f"Transfer of {amount:.2f}€ to {target_account.iban}")

    def show(self):
        """Shows account information."""
        print(f"IBAN: {self._iban}")
        print(f"Balance: {self._balance:.2f}€")


# ====================
# USAGE EXAMPLE
# ====================

if __name__ == "__main__":
    print("=== Version 3: Modular ===\n")

    # Now we use valid IBANs (with correct checksum)
    # You can generate test IBANs at: https://www.generateiban.com/
    account1 = BankAccount("ES9121000418450200051332", 1000)
    account2 = BankAccount("ES7921000813610123456789", 500)

    print("Account 1:")
    account1.show()
    print()

    print("Account 2:")
    account2.show()
    print()

    # Operations
    print("--- Operations ---")
    account1.deposit(200)
    account1.withdraw(150)
    account1.transfer(account2, 100)
    print()

    print("--- Final State ---")
    print("Account 1:")
    account1.show()
    print()
    print("Account 2:")
    account2.show()
    print()

    # Validation tests
    print("--- Validation ---")

    # IBAN with correct format but incorrect checksum
    try:
        invalid = BankAccount("ES1234567890123456789012", 100)
    except ValueError as e:
        print(f"✓ Detected IBAN with incorrect checksum: {e}")

    # IBAN with incorrect format
    try:
        invalid2 = BankAccount("ES123", 100)
    except ValueError as e:
        print(f"✓ Detected IBAN with incorrect format: {e}")

    # Insufficient funds
    try:
        account1.withdraw(10000)
    except InsufficientFundsError as e:
        print(f"✓ Funds control: {e}")

