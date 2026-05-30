class Calculator:
    def divide(self, a, b):
        if b == 0:
            print("Bo'lishda xatolik")
        else:
            return a / b
    
calc = Calculator()
print(calc.divide(15, 3))
print(calc.divide(15, 0))