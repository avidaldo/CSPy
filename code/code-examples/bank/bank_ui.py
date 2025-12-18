from bank_oop import BankAccount, InsufficientFundsError


def print_menu():
    print("\nBank Account CLI Menu:")
    print("1. Show account info")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Show balance")
    print("5. Exit")


def get_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))
            if amount <= 0:
                print("Amount must be positive.")
                continue
            return amount
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    try:
        account = BankAccount("12345678A", "ES7620770024003102575766", 1000.0)
        print("Welcome to the Bank CLI!")
        while True:
            print_menu()
            choice = input("Select an option (1-5): ").strip()
            if choice == "1":
                print("\nAccount Information:")
                print(account)
            elif choice == "2":
                amount = get_amount("Enter amount to deposit: $")
                account.deposit(amount)
                print(
                    f"Deposited ${amount:.2f}. New balance: ${account.balance:.2f}"
                )
            elif choice == "3":
                amount = get_amount("Enter amount to withdraw: $")
                try:
                    account.withdraw(amount)
                    print(
                        f"Withdrew ${amount:.2f}. New balance: ${account.balance:.2f}"
                    )
                except InsufficientFundsError as e:
                    print(f"Transaction Error: {e}")
            elif choice == "4":
                print(f"Current balance: ${account.balance:.2f}")
            elif choice == "5":
                print("Thank you for using the Bank CLI. Goodbye!")
                break
            else:
                print("Invalid option. Please select 1-5.")
    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
