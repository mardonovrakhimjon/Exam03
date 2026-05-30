class Animals:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

animal01 = Animals("dog", "cat!")

def make_sound():
    print(f"{animal01.name} says {animal01.sound} ")

make_sound()