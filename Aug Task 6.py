import math

class Shape:
    def calculate_area(self, *args):
        print(f"Shape")

class Square(Shape):

    def __init__(self):
        self.side = None

    def calculate_area(self, side):
        self.side = side
        return self.side ** 2

class Triangle(Shape):

    def __init__(self):
        self.height = None
        self.base = None

    def calculate_area(self, base, height):
        self.base = base
        self.height = height
        return 0.5 * self.base * self.height

class Circle(Shape):

    def __init__(self):
        self.radius = None

    def calculate_area(self, radius):
        self.radius = radius
        return math.pi * (self.radius ** 2)

print(f"Area of Square: {Square().calculate_area(float(input('Side of Square: ')))}")
print(f"Area of Triangle: {Triangle().calculate_area(float(input('Base of Triangle: ')), float(input('Height of Triangle: ')))}")
print(f"Area of Circle: {Circle().calculate_area(float(input('Radius of Circle: ')))}")
