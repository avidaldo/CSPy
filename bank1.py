import re


# Function to validate Spanish DNI
def validate_dni(dni: str) -> bool:
    """Validate a Spanish DNI (8 digits followed by a letter)."""
    pattern = r'^[0-9]{8}[A-Z]$'
    return bool(re.match(pattern, dni))


# Data: separate variables for each piece of information
account1_dni: str = "12345678A"
account1_balance: float = 1000.0

account2_dni: str = "87654321B"
account2_balance: float = 500.0

# Validate DNIs
if not validate_dni(account1_dni):
    raise ValueError("Invalid DNI for account 1.")
if not validate_dni(account2_dni):
    raise ValueError("Invalid DNI for account 2.")


# Functions to work with accounts
def deposit(balance: float, amount: float) -> float:
    """Add money to an account and return new balance."""
    if amount > 0:
        return balance + amount
    return balance


def withdraw(balance: float, amount: float) -> float:
    """Remove money from an account and return new balance."""
    if amount > 0 and amount <= balance:
        return balance - amount
    return balance


def show_account(dni: str, balance: float) -> None:
    """Display account information."""
    print(f"Account DNI: {dni}")
    print(f"Balance: ${balance:.2f}")


# Using the functions
show_account(account1_dni, account1_balance)
show_account(account2_dni, account2_balance)
