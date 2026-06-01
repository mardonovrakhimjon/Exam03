class Bird:
    def speak(self):
        return "Chirq Chirq"


class Dog(Bird):
    def speak(self):
        return "Woof Woof"

hayvonlar = [
    Bird(), Dog()
]

for hayvon in hayvonlar:
    print(hayvon.speak())