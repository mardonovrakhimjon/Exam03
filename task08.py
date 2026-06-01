class Rectangle:
    def __init__(self, width, height):
        self.width  = width
        self.height = height

    def area(self):
        return self.width*self.height

turtburchak1 = Rectangle(13, 6)
turtburchak2 = Rectangle(9, 4)

print(turtburchak1.area())
print(turtburchak2.area())