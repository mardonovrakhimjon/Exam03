class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.modul = model

    def move(self):
        return "Vehicle is moving"

class Car(Vehicle):
    def move(self):
        return "Car is driving"

transport = Vehicle("Generic", "X-Model")
print(transport.move())

# Car mashinasi
mashina = Car("Chevrolet", "Gentra")
print(mashina.move())