"""
Version 2: Functional
=====================
Validation is extracted to independent functions.
This improves Separation of Concerns (SoC).

Improvements over v1:
- Validation functions can be reused
- BankAccount class is simpler and more focused
- Testing validations is easier
"""
import re

# ====================
# VALIDATION FUNCTIONS
# ====================


def validate_iban_format(iban):
    """
    Validates the format of a Spanish IBAN.
    
    Args:
        iban: String with the IBAN to validate
    
    Returns:
        bool: True if format is correct
    """
    pattern = r'^ES\d{22}$'
    return bool(re.match(pattern, iban))


def validate_positive_amount(amount):
    """
    Validates that an amount is positive.
    
    Args:
        amount: Amount to validate
    
    Returns:
        bool: True if positive
    """
    return amount > 0


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
    
    Functional version: uses external functions for validation.
    The class focuses only on bank account logic.
    """

    def __init__(self, iban, initial_balance=0):
        """
        Creates a new bank account.
        
        Args:
            iban: Spanish IBAN (ES + 22 digits)
            initial_balance: Initial balance (default 0)
        """
        # Use external validation functions
        if not validate_iban_format(iban):
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
    print("=== Version 2: Functional ===\n")

    # Create accounts
    account1 = BankAccount("ES1234567890123456789012", 1000)
    account2 = BankAccount("ES9876543210987654321098", 500)

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

    # Now we can test functions directly
    assert validate_iban_format("ES1234567890123456789012") == True
    assert validate_iban_format("ES123") == False
    assert validate_positive_amount(100) == True
    assert validate_positive_amount(-50) == False
    print("✓ All validations passed")

    try:
        invalid = BankAccount("ES123", 100)
    except ValueError as e:
        print(f"✓ IBAN Validation: {e}")

    try:
        account1.withdraw(10000)
    except InsufficientFundsError as e:
        print(f"✓ Funds control: {e}")

