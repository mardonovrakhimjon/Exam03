class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} so'm qo'shildi. Joriy balans: {self.balance} so'm")
        else:
            print("Xato: Qo'shilayotgan summa noldan katta bo'lishi kerak!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Balans yetarli emas")
        elif amount <= 0:
            print("Xato: Yechilayotgan summa noldan katta bo'lishi kerak!")
        else:
            self.balance -= amount
            print(f"{amount} so'm yechildi. Joriy balans: {self.balance} so'm")



hisob = BankAccount("Ali", 50000)

hisob.deposit(20000)

hisob.withdraw(40000)

hisob.withdraw(100000)
