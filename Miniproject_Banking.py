class BankAccount:
    def __init__(self, account_number, pin):
        self.account_number = account_number
        self.pin = pin
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited ₹{:.2f}.\nNew balance is ₹{:.2f}.".format(amount, self.balance))
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("Withdrew ₹{:.2f}.\nNew balance is ₹{:.2f}.".format(amount, self.balance))
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        print("Your balance is ₹{:.2f}.".format(self.balance))
        return self.balance

def login(account_list, account_number, pin):
    for account in account_list:
        if account.account_number == account_number and account.pin == pin:
            print("Login successful.")
            return account
    print("Invalid account number or pin.")
    return None

def main():
    accounts = [
        BankAccount("1234567890", "1234"),
        BankAccount("2345678910", "2345"),
        BankAccount("3456789120", "3456")
    ]

    print("Welcome to the banking system")
    account_number = input("Enter your account number: ")
    pin = input("Enter your pin: ")

    account = login(accounts, account_number, pin)
    if not account:
        return

    while True:
        print("\n1. Deposit Amount")
        print("\n2. Withdraw Amount")
        print("\n3. Check Balance")
        print("\n4. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == "3":
            account.get_balance()
        elif choice == "4":
            print("You have successfully logged out.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
