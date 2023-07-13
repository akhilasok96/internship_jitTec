class Bank:
    def __init__(self):
        self.customers = []

    # def displayCustomers(self):
    #     print(self.customers)

    def create_account(self, name, initial_deposit):
        account = [name, initial_deposit]
        self.customers.append(account)
        print(f"Account created for {name} with an initial deposit of {initial_deposit}")

    def deposit(self, name, amount):
        for customer in self.customers:
            if customer[0] == name:
                customer[1] += amount
                print(f"Deposited {amount} into {name}'s account.")
                return
        print(f"Customer {name} not found.")

    def withdraw(self, name, amount):
        for customer in self.customers:
            if customer[0] == name:
                if customer[1] >= amount and customer[1] - amount >= 0:
                    customer[1] -= amount
                    print(f"Withdrew {amount} from {name}'s account.")
                    return
                else:
                    print(f"Insufficient balance for {name}.")
                    return
        print(f"Customer {name} not found.")

    def displayAccountDetails(self, name):
        for customer in self.customers:
            if customer[0] == name:
                print(f"Account details for {name}:")
                print(f"Balance: ${customer[1]}")
                return
        print(f"Customer {name} not found.")

def recpt():
    print("******* MENU *******")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Display Account")
    print("5. Display Customers")
    print("6. Exit")
    opt = int(input("Select an option: "))
    match opt:
        case 1:
            name = input("Enter the name: ")
            deposit = int(input("Enter the initial deposit: "))
            global bank
            bank = Bank()
            bank.create_account(name, deposit)
        case 2:
            name= input("Enter the customer name: ")
            amt = int(input("Enter the amount to be deposited: "))
            bank.deposit(name, amt)
        case 3:
            name = input("Enter the customer name: ")
            amt = int(input("Enter the amount to be withdrawn: "))
            bank.withdraw(name, amt)
        case 4:
            name = input("Enter the customer name: ")
            bank.displayAccountDetails(name)
        case 5:
            bank.displayCustomers()
        case 6:
            exit()

cn = "yes"
while cn == "yes":
    cn = input("Do you want to use the bank app ? (yes/no) : ")
    if cn == "yes":
        recpt()
    else:
        print("Banking app closed")