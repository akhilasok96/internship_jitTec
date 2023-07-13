class Account:
    def __init__(self, account_number, customer_name, balance=0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of {amount} successful.")
        else:
            print("Invalid amount. Deposit failed.")

    def withdraw(self, amount):
            self.balance -= amount

    def display_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Balance: {self.balance}")

class SavingsAccount(Account):
    def __init__(self, account_number, customer_name, accType, balance=0):
        super().__init__(account_number, customer_name, balance)
        self.accType = accType
        self.minBalance = 1000
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance and (self.balance - amount) >= 0 and (self.balance - amount) > self.minBalance:
            super().withdraw(amount)
            print(f"Amount of {amount} withdrawn successfully")
        else: 
            print("Insufficient balance or invalid amount. Withdrawal failed.")
            
class CurrentAccount(Account):
    def __init__(self, account_number, customer_name, accType, balance=0):
        super().__init__(account_number, customer_name, balance)
        self.accType = accType
        self.overDraft = -500

    def withdraw(self, amount):
        if amount > 0 and (self.balance - amount) >= self.overDraft:
            super().withdraw(amount)
            print(f"Amount of {amount} withdrawn successfully")
        else: 
            print("Insufficient balance or invalid amount. Withdrawal failed.")

class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self):
        accType = input("Enter the type of account: ")
        account_number = int(input("Enter account number: "))
        customer_name = input("Enter customer name: ")
        if accType == "savings":
            self.accounts.append(SavingsAccount(account_number,customer_name, accType))
            print("Savings account created successfully.")
        else:
            self.accounts.append(CurrentAccount(account_number,customer_name, accType))
            print("Current account created successfully.")

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def deposit(self):
        account_number = int(input("Enter account number: "))
        account = self.find_account(account_number)
        if account:
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        else:
            print("Account not found.")

    def withdraw(self):
        account_number = int(input("Enter account number: "))
        account = self.find_account(account_number)
        if account:
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        else:
            print("Account not found.")

    def display_details(self):
        account_number = int(input("Enter account number: "))
        account = self.find_account(account_number)
        if account:
            account.display_details()
        else:
            print("Account not found.")

def main():
    bank = Bank()
    while True:
        print("\n===== Bank Menu =====")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Display Account Details")
        print("5. Exit")

        choice = int(input("Enter your choice (1-5): "))

        match choice:
            case 1:
                bank.create_account()
            case 2:
                bank.deposit()
            case 3:
                bank.withdraw()
            case 4:
                bank.display_details()
            case 5:
                print("Exiting the program...")
                break
main()
