class BankAccount:
    default_acc_no = 0
    def __init__(self,name,balance):
        self.user_name = name
        self.balance = balance
        BankAccount.default_acc_no = BankAccount.default_acc_no + 1
    
    def display(self):
        print("Account Number:",BankAccount.default_acc_no)
        print("Name:",self.user_name)
        print("Amount:",self.balance)
    
    def deposite(self,amount):
        self.balance += amount
        return self.balance

    def withdraw(self,amount):
        if self.balance < amount:
            print("Not sufficent balance!! ")
        else:
            print("Account Number:",BankAccount.default_acc_no)
            self.balance -= amount
        return self.balance

b1 = BankAccount("Rohit", 20000)
b1.display()
print(b1.deposite(500))
print(b1.withdraw(200))



        