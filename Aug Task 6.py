import math

class Shape:
    def calculate_area(self, *args):
        print(f"{Shape.__name__}")

class Square(Shape):

    def calculate_area(self, side):
        print(f"{self.__class__.__name__} (Child) calculates the area.")
        return side ** 2

class Triangle(Shape):

    def calculate_area(self, base, height):
        print(f"{self.__class__.__name__} (Child) calculates the area.")
        return 0.5 * base * height

class Circle(Shape):

    def calculate_area(self, radius):
        print(f"{self.__class__.__name__} (Child) calculates the area.")
        return math.pi * radius ** 2

print(f"Area of Square: {Square().calculate_area(float(input('Side of Square: ')))}")
print(f"Area of Triangle: {Triangle().calculate_area(float(input('Base of Triangle: ')), float(input('Height of Triangle: ')))}")
print(f"Area of Circle: {Circle().calculate_area(float(input('Radius of Circle: ')))}")
