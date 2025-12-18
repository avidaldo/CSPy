import tkinter as tk
from tkinter import messagebox, ttk
from bank_domain import InsufficientFundsError
from bank_manager import BankManager


class BankGUI:

    def __init__(self, root, bank_manager: BankManager):
        self.root = root
        self.root.title("Bank Account Manager")
        self.root.geometry("600x550")

        # Use the bank manager service layer
        self.bank_manager = bank_manager
        self.current_account = None

        # Set default account if any exists
        accounts = self.bank_manager.get_all_accounts()
        if accounts:
            self.current_account = list(accounts.values())[0]

        # Title label
        title_label = tk.Label(root,
                               text="Bank Account Manager",
                               font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        # Account selection frame
        selection_frame = tk.LabelFrame(root,
                                        text="Account Selection",
                                        padx=10,
                                        pady=10)
        selection_frame.pack(padx=10, pady=5, fill="x")

        tk.Label(selection_frame, text="Select Account:").pack(side=tk.LEFT)
        self.account_combo = ttk.Combobox(selection_frame,
                                          width=25,
                                          state="readonly")
        self.account_combo.pack(side=tk.LEFT, padx=5)
        self.account_combo.bind("<<ComboboxSelected>>", self.on_account_select)
        self.update_account_list()

        # Create new account button
        create_btn = tk.Button(selection_frame,
                               text="Create New Account",
                               command=self.show_create_account_dialog,
                               bg="#FF9800",
                               fg="white")
        create_btn.pack(side=tk.LEFT, padx=5)

        # Balance display
        self.balance_label = tk.Label(
            root,
            text=f"Balance: ${self.current_account.balance:.2f}",
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
        if self.current_account:
            self.balance_label.config(
                text=f"Balance: ${self.current_account.balance:.2f}")

    def update_account_list(self):
        """Update the account combobox with all accounts."""
        accounts = self.bank_manager.get_all_accounts()
        account_list = [f"{dni} - {acc.iban}" for dni, acc in accounts.items()]
        self.account_combo['values'] = account_list
        if self.current_account:
            current_index = list(accounts.keys()).index(
                self.current_account.dni)
            self.account_combo.current(current_index)

    def on_account_select(self, event):
        """Handle account selection from combobox."""
        selected = self.account_combo.get()
        if selected:
            dni = selected.split(" - ")[0]
            self.current_account = self.bank_manager.get_account(dni)
            self.update_balance_display()

    def show_create_account_dialog(self):
        """Show dialog to create a new account."""
        dialog = tk.Toplevel(self.root)
        dialog.title("Create New Account")
        dialog.geometry("400x250")
        dialog.grab_set()

        # DNI entry
        tk.Label(dialog, text="DNI (8 digits + letter):").grid(row=0,
                                                               column=0,
                                                               padx=10,
                                                               pady=10,
                                                               sticky="w")
        dni_entry = tk.Entry(dialog, width=25)
        dni_entry.grid(row=0, column=1, padx=10, pady=10)

        # IBAN entry
        tk.Label(dialog, text="IBAN (ES + 22 digits):").grid(row=1,
                                                             column=0,
                                                             padx=10,
                                                             pady=10,
                                                             sticky="w")
        iban_entry = tk.Entry(dialog, width=25)
        iban_entry.grid(row=1, column=1, padx=10, pady=10)

        # Initial balance entry
        tk.Label(dialog, text="Initial Balance ($):").grid(row=2,
                                                           column=0,
                                                           padx=10,
                                                           pady=10,
                                                           sticky="w")
        balance_entry = tk.Entry(dialog, width=25)
        balance_entry.insert(0, "0")
        balance_entry.grid(row=2, column=1, padx=10, pady=10)

        def create_account():
            try:
                dni = dni_entry.get().strip().upper()
                iban = iban_entry.get().strip().upper()
                balance = float(balance_entry.get())

                new_account = self.bank_manager.create_account(
                    dni, iban, balance)
                self.current_account = new_account
                self.update_account_list()
                self.update_balance_display()
                messagebox.showinfo(
                    "Success", f"Account created successfully!\nDNI: {dni}")
                dialog.destroy()
            except ValueError as e:
                messagebox.showerror("Error", str(e))

        # Buttons
        btn_frame = tk.Frame(dialog)
        btn_frame.grid(row=3, column=0, columnspan=2, pady=20)

        tk.Button(btn_frame,
                  text="Create",
                  command=create_account,
                  bg="#4CAF50",
                  fg="white",
                  width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame,
                  text="Cancel",
                  command=dialog.destroy,
                  bg="#9E9E9E",
                  fg="white",
                  width=10).pack(side=tk.LEFT, padx=5)

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
        if not self.current_account:
            messagebox.showerror("Error", "No account selected.")
            return

        amount = self.get_amount()
        if amount is not None:
            try:
                self.current_account.deposit(amount)
                self.update_balance_display()
                self.amount_entry.delete(0, tk.END)
                messagebox.showinfo(
                    "Success",
                    f"Deposited ${amount:.2f}\nNew balance: ${self.current_account.balance:.2f}"
                )
            except ValueError as e:
                messagebox.showerror("Error", str(e))

    def withdraw(self):
        """Handle withdraw operation."""
        if not self.current_account:
            messagebox.showerror("Error", "No account selected.")
            return

        amount = self.get_amount()
        if amount is not None:
            try:
                self.current_account.withdraw(amount)
                self.update_balance_display()
                self.amount_entry.delete(0, tk.END)
                messagebox.showinfo(
                    "Success",
                    f"Withdrew ${amount:.2f}\nNew balance: ${self.current_account.balance:.2f}"
                )
            except InsufficientFundsError as e:
                messagebox.showerror("Insufficient Funds", str(e))
            except ValueError as e:
                messagebox.showerror("Error", str(e))

    def show_account_info(self):
        """Display complete account information."""
        if not self.current_account:
            messagebox.showerror("Error", "No account selected.")
            return
        info = str(self.current_account)
        messagebox.showinfo("Account Information", info)


def main():
    # Initialize the service layer
    bank_manager = BankManager()

    # Create a default account for demo purposes
    try:
        bank_manager.create_account("12345678A", "ES7620770024003102575766",
                                    1000.0)
    except ValueError:
        pass  # Account already exists

    # Initialize GUI with the bank manager
    root = tk.Tk()
    app = BankGUI(root, bank_manager)
    root.mainloop()


if __name__ == "__main__":
    main()
