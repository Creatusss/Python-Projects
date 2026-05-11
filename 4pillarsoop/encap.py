class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def ChkBalance(self):
        return self.__balance
    
account1 = BankAccount(1000)
account1.deposit(100)
print(account1.ChkBalance())

account2 = BankAccount(500)
account2.deposit(500)
print(account2.ChkBalance())