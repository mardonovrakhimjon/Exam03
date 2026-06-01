class Calculator:
    def divide(self, a, b):
        if b == 0:
            return "Bo‘lishda xatolik"
        else:
            return a/b

kal = Calculator()

print(kal.divide(125, 5))
print(kal.divide(12, 0))