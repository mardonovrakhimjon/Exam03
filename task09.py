class Animal:
    def __init__(self, name, sound):
        self.name  = name
        self.sound = sound

    def make_sound(self):
        return f"{self.name} says {self.sound}!"


it = Animal("dog", "woof-woof")
mushuk = Animal("Cat", "meyav-meyav")

print(it.make_sound())
print(mushuk.make_sound())