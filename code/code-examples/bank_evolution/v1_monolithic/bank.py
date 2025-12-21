"""
Version 1: Monolithic
=====================
All code is in one class. IBAN validation is inside the class.
This works for starting, but has organization problems.
"""
import re


class InsufficientFundsError(Exception):
    """Raised when there are insufficient funds for an operation."""
    pass


class BankAccount:
    """
    Bank account identified by IBAN.
    
    Monolithic version: all logic is inside the class,
    including IBAN validation.
    """

    def __init__(self, iban, initial_balance=0):
        """
        Creates a new bank account.
        
        Args:
            iban: Spanish IBAN (ES + 22 digits)
            initial_balance: Initial balance (default 0)
        """
        # Inline validation - everything is inside the class
        if not self._is_valid_iban(iban):
            raise ValueError(f"Invalid IBAN: {iban}")

        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")

        self._iban = iban
        self._balance = initial_balance

    def _is_valid_iban(self, iban):
        """
        Validates a Spanish IBAN (basic format).
        Simple version: only checks format with regex.
        """
        # Only format: ES + 22 digits
        pattern = r'^ES\d{22}$'
        return bool(re.match(pattern, iban))

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
        if amount <= 0:
            raise ValueError("Amount must be positive")

        self._balance += amount
        print(f"Deposit: {amount:.2f}€. New balance: {self._balance:.2f}€")

    def withdraw(self, amount):
        """Withdraws money from the account."""
        if amount <= 0:
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

        # Withdraw from this account
        self.withdraw(amount)
        # Deposit into target account
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
    print("=== Version 1: Monolithic ===\n")

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

    # Validation tests (using asserts as in module notebooks)
    print("--- Validation ---")
    try:
        invalid = BankAccount("ES123", 100)  # Incorrect IBAN
    except ValueError as e:
        print(f"✓ Validation correct: {e}")

    try:
        account1.withdraw(10000)  # Insufficient funds
    except InsufficientFundsError as e:
        print(f"✓ Funds control correct: {e}")

