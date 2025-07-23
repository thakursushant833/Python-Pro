class Bank_Account:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
        else:
            print("No Suficent Amount")
    def display(self):
        print(f"Name={self.name}")
        print(f"Current Amount={self.balance}")
acc=Bank_Account("Ram",1000)
acc.deposit(100)
acc.withdraw(200)
acc.display()