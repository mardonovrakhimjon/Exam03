class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        return "Vehicle is moving"

class Car(Vehicle):

    def move(self):
        return "Car is driving"

mashina1 = Vehicle("Matiz", "daewoo")
mashina2 = Car("Shivam Nexa", "Suzuki")

print(mashina1.move())
print(mashina2.move())