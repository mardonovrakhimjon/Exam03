class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

obyekt01 = Rectangle(3, 5)
def area():
    print(f"obyekt01 ning areasi {obyekt01.width * obyekt01.height}")

area()