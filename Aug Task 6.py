import math

class Shape:
    def calculate_area(self, *args):
        pass

class Square(Shape):

    def calculate_area(self, side):
        return side ** 2

class Triangle(Shape):

    def calculate_area(self, base, height):
        return 0.5 * base * height

class Circle(Shape):

    def calculate_area(self, radius):
        return math.pi * radius ** 2

print(f"Area of Square: {Square().calculate_area(float(input('Side of Square: ')))}")
print(f"Area of Triangle: {Triangle().calculate_area(float(input('Base of Triangle: ')), float(input('Height of Triangle: ')))}")
print(f"Area of Circle: {Circle().calculate_area(float(input('Radius of Circle: ')))}")
