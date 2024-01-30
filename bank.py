class Bank_Account():
   def __init__(self,balance,amount):
      self.balance=balance
      self.amount=amount
print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
def deposit(self):
 amount=float(input("Enter amount to be Deposited: "))
 self.balance += self.amount
 print("\n Amount Deposited:",self.amount)
def withdraw(self):
 amount = float(input("Enter amount to be Withdrawn: "))
 if( self.balance>=self.amount):
  self.balance=self.balance-self.amount
  print("\n You Withdrew:", self.amount)
 else:
  print("\n Insufficient balance ")
def display(self):
 print("\n Net Available Balance=",self.balance)
# creating an object of class
s = Bank_Account()
# Calling functions with that class object
s.deposit(balance,amount)
s.withdraw()
s.display()
