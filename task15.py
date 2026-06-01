class Phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_info(self):
        print(f"Phone: {self.brand} {self.model}")

phone = Phone("Samsung", "Galaxy S26")

phone.show_info()