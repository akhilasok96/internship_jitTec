banks = {}
def createAccount():
    account = []
    
    cid = int(input("Enter your id: "))
    name = input("Enter your name: ")
    balance = int(input("Enter your balance: "))
    account.append(name)
    account.append(balance)
    banks.update({cid: account})
    print(banks)

def deposit(cid, amt):
    for x in banks:
        if x["id"] == cid:
            x["id"][1] += amt
    print(banks)
 
def withdraw(cid, amt):
    for x in banks:
        if x["id"] == cid:
            if(x["balance"] - amt >= 0):
              x["balance"] -= amt
            else:
                print(f"Minimum balance reached. You cannot withdraw {amt}") 
    print(banks)

def bankapp():
    print("******* MENU *******")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    opt = int(input("Select an option: "))
    match opt:
        case 1:
            createAccount()
        case 2:
            cid = int(input("Enter the customer id: "))
            amt = int(input("Enter the amount to be deposited: "))
            deposit(cid, amt)
        case 3:
            cid = int(input("Enter the customer id: "))
            amt = int(input("Enter the amount to be withdrawn: "))
            withdraw(cid, amt)
        case 4:
            exit()
      
cn = "yes"
while cn == "yes":
    cn = input("Do you want to use the bank app ? (yes/no) : ")
    if cn == "yes":
        bankapp()
    else:
        print("Banking app closed")

