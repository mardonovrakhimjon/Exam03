class BankAccount:
    def __init__(self, owner, balance):
        self.owner   = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return("Balans yetarli emas")
        else:
            self.balance -= amount

hisob = BankAccount("ali", 50000)
hisob.deposit(200000)

print(hisob.withdraw(30000))
print(hisob.balance)