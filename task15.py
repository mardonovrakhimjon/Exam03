class Phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model  

    def show_info(self):
        print(self.brand, self.model)

p01 = Phone("Samsung", "Galaxy S21")

p01.show_info()