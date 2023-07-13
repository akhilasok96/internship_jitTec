import random

class Bankx:
    customers = []
        
    def bankMenu(self):
      print("******* MENU *******")
      print("1. Create Account")
      print("2. Deposit")
      print("3. Withdraw")
      print("4. Display Account")
      print("5. Exit")
      opt = int(input("Select an option: "))
      match opt:
          case 1:
              cid  = random.randrange(100, 250)
              name  = input("Enter the customer name: ")
              deposit  = int(input("Enter the initial deposit: "))
              print("Account Created")
              print("Id: "+str(cid)+" | Name: "+name+" | Balance: "+str(deposit))
              a = Account(cid, name, deposit)
              self.customers.append(a)
   
          case 2:
              cid = int(input("Enter the customer id: "))
              amt = int(input("Enter the amount to be deposited: "))
              print(len(self.customers))
              for x in self.customers:
                  print(x.getId())
                  if x.getId() == cid:
                      x.deposit(cid, amt)
          case 3:
              cid = int(input("Enter the customer id: "))
              amt = int(input("Enter the amount to be withdrawn: "))
              for x in self.customers:
                  if x.getId() == cid:
                      x.withdraw(cid, amt)
          case 4:
              cid = int(input("Enter the customer id: "))
              for x in self.customers:
                  if x.getId() == cid:
                      x.displayAccountDetails(cid)
          case 5:
              exit()
    
class Account:
    def __init__(self, cid, name, deposit):
        self.cid = cid
        self.name = name
        self.deposit = deposit
    
    def getId(self):
        return self.cid
      
    def deposit(self, cid, amt):
        if self.cid == cid:
            print("updating obj")
            self.deposit += amt
    
    def withdraw(self, cid, amt):
        if self.cid == cid and self.deposit - amt >= 0:
            self.deposit -= amt
    
    def displayAccountDetails(self, cid):
        if self.cid == cid:
            print("Id", self.cid, "Name", self.name, "Amount", self.deposit, sep=" | ")

cn = "yes"
while cn == "yes":
    cn = input("Do you want to use the bank app ? (yes/no) : ")
    if cn == "yes":
        d = Bankx()
        d.bankMenu()
    else:
        print("Banking app closed")