"""
Bank Manager - Service Layer
Handles business logic for managing multiple bank accounts.
"""
from bank_domain import BankAccount


class BankManager:
    """Manages multiple bank accounts."""

    def __init__(self):
        """Initialize the bank manager with an empty account registry."""
        self._accounts = {}

    def create_account(self,
                       dni: str,
                       iban: str,
                       initial_balance: float = 0) -> BankAccount:
        """
        Create a new bank account.
        
        Args:
            dni: Spanish DNI (8 digits + letter)
            iban: Spanish IBAN (ES + 22 digits)
            initial_balance: Initial account balance
            
        Returns:
            The newly created BankAccount
            
        Raises:
            ValueError: If account with this DNI already exists or validation fails
        """
        if dni in self._accounts:
            raise ValueError(f"Account with DNI {dni} already exists.")

        account = BankAccount(dni, iban, initial_balance)
        self._accounts[dni] = account
        return account

    def get_account(self, dni: str) -> BankAccount:
        """
        Retrieve an account by DNI.
        
        Args:
            dni: The DNI of the account to retrieve
            
        Returns:
            The BankAccount associated with the DNI
            
        Raises:
            KeyError: If no account exists with the given DNI
        """
        if dni not in self._accounts:
            raise KeyError(f"No account found with DNI {dni}.")
        return self._accounts[dni]

    def get_all_accounts(self) -> dict[str, BankAccount]:
        """
        Get all registered accounts.
        
        Returns:
            Dictionary mapping DNI to BankAccount
        """
        return self._accounts.copy()

    def account_exists(self, dni: str) -> bool:
        """
        Check if an account exists with the given DNI.
        
        Args:
            dni: The DNI to check
            
        Returns:
            True if account exists, False otherwise
        """
        return dni in self._accounts

    def delete_account(self, dni: str) -> bool:
        """
        Delete an account by DNI.
        
        Args:
            dni: The DNI of the account to delete
            
        Returns:
            True if account was deleted, False if it didn't exist
        """
        if dni in self._accounts:
            del self._accounts[dni]
            return True
        return False

    def get_account_count(self) -> int:
        """
        Get the total number of accounts.
        
        Returns:
            The number of registered accounts
        """
        return len(self._accounts)
