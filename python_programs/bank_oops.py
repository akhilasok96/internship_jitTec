mainAcc = []

class Bank:
    def __init__(self, acc):
        self.acc = acc
        self.mainAcc = mainAcc.append(acc)

    def searchAcc(self, cid):
       for x in mainAcc:
           if x[0] == cid:
               print(x[0], x[1], x[2], sep=" | ")
    
    def printMainAcc(self):
        print(mainAcc)
    
    def withdraw(self, cid, amt):
        for x in mainAcc:
            if x[0] == cid and x[2] - amt >= 0:
                x[2] -= amt
    
    def deposit(self, cid, amt):
        for x in mainAcc:
            if x[0] == cid:
                x[2] += amt
  

def recpt():
    print("******* MENU *******")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Display Accounts")
    print("5. Search Account")
    print("6. Exit")
    opt = int(input("Select an option: "))
    match opt:
        case 1:
            account = []
            account.append(int(input("Enter the customer id: ")))
            account.append(input("Enter the customer name: "))
            account.append(int(input("Enter the balance: ")))
            global d
            d = Bank(account)
        case 2:
            cid = int(input("Enter the customer id: "))
            amt = int(input("Enter the amount to be deposited: "))
            d.deposit(cid, amt)
        case 3:
            cid = int(input("Enter the customer id: "))
            amt = int(input("Enter the amount to be withdrawn: "))
            d.withdraw(cid, amt)
        case 4:
            d.printMainAcc()
        case 5:
            cid = int(input("Enter the customer id: "))
            d.searchAcc(cid)
        case 6:
            exit()

cn = "yes"
while cn == "yes":
    cn = input("Do you want to use the bank app ? (yes/no) : ")
    if cn == "yes":
        recpt()
    else:
        print("Banking app closed")