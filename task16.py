class Bird:
    def speak(self):
        return "Qag'-qag'"

class Dog:
    def speak(self):
        return "Vaf-vaf"

birds_dogs = [Bird(), Dog()]

for b_d in birds_dogs:
    print(b_d.speak())