import tkinter as tk
from tkinter import messagebox
from bank_domain import BankAccount, InsufficientFundsError


class BankGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Bank Account")
        self.root.geometry("400x400")

        # Create account with default values (same as CLI)
        self.account = BankAccount("12345678A", "ES7620770024003102575766",
                                   1000.0)

        # Title label
        title_label = tk.Label(root,
                               text="Bank Account Manager",
                               font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        # Balance display
        self.balance_label = tk.Label(
            root,
            text=f"Balance: ${self.account.balance:.2f}",
            font=("Arial", 14))
        self.balance_label.pack(pady=10)

        # Amount entry
        amount_frame = tk.Frame(root)
        amount_frame.pack(pady=10)
        tk.Label(amount_frame, text="Amount: $").pack(side=tk.LEFT)
        self.amount_entry = tk.Entry(amount_frame, width=15)
        self.amount_entry.pack(side=tk.LEFT, padx=5)

        # Buttons frame
        buttons_frame = tk.Frame(root)
        buttons_frame.pack(pady=20)

        # Deposit button
        deposit_btn = tk.Button(buttons_frame,
                                text="Deposit",
                                width=15,
                                command=self.deposit,
                                bg="#4CAF50",
                                fg="white")
        deposit_btn.pack(pady=5)

        # Withdraw button
        withdraw_btn = tk.Button(buttons_frame,
                                 text="Withdraw",
                                 width=15,
                                 command=self.withdraw,
                                 bg="#f44336",
                                 fg="white")
        withdraw_btn.pack(pady=5)

        # Show account info button
        info_btn = tk.Button(buttons_frame,
                             text="Show Account Info",
                             width=15,
                             command=self.show_account_info,
                             bg="#2196F3",
                             fg="white")
        info_btn.pack(pady=5)

        # Exit button
        exit_btn = tk.Button(buttons_frame,
                             text="Exit",
                             width=15,
                             command=root.quit,
                             bg="#9E9E9E",
                             fg="white")
        exit_btn.pack(pady=5)

    def update_balance_display(self):
        """Update the balance label."""
        self.balance_label.config(text=f"Balance: ${self.account.balance:.2f}")

    def get_amount(self):
        """Get and validate amount from entry field."""
        try:
            amount = float(self.amount_entry.get())
            if amount <= 0:
                messagebox.showerror("Error", "Amount must be positive.")
                return None
            return amount
        except ValueError:
            messagebox.showerror("Error",
                                 "Invalid input. Please enter a number.")
            return None

    def deposit(self):
        """Handle deposit operation."""
        amount = self.get_amount()
        if amount is not None:
            try:
                self.account.deposit(amount)
                self.update_balance_display()
                self.amount_entry.delete(0, tk.END)
                messagebox.showinfo(
                    "Success",
                    f"Deposited ${amount:.2f}\nNew balance: ${self.account.balance:.2f}"
                )
            except ValueError as e:
                messagebox.showerror("Error", str(e))

    def withdraw(self):
        """Handle withdraw operation."""
        amount = self.get_amount()
        if amount is not None:
            try:
                self.account.withdraw(amount)
                self.update_balance_display()
                self.amount_entry.delete(0, tk.END)
                messagebox.showinfo(
                    "Success",
                    f"Withdrew ${amount:.2f}\nNew balance: ${self.account.balance:.2f}"
                )
            except InsufficientFundsError as e:
                messagebox.showerror("Insufficient Funds", str(e))
            except ValueError as e:
                messagebox.showerror("Error", str(e))

    def show_account_info(self):
        """Display complete account information."""
        info = str(self.account)
        messagebox.showinfo("Account Information", info)


def main():
    root = tk.Tk()
    app = BankGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
