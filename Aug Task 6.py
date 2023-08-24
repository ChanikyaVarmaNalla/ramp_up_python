import math

class Shape:
    def calculate_area(self, *args):
        print(f"Shape")

class Square(Shape):
    def calculate_area(self, side=None):
        if side is not None:
            self.side = side
            return self.side ** 2
        else:
            return super().calculate_area()

class Triangle(Shape):
    def calculate_area(self, base=None, height=None):
        if base is not None and height is not None:
            self.base = base
            self.height = height
            return 0.5 * self.base * self.height
        else:
            return super().calculate_area()

class Circle(Shape):
    def calculate_area(self, radius=None):
        if radius is not None:
            self.radius = radius
            return math.pi * (self.radius ** 2)
        else:
            return super().calculate_area()

square = Square()
triangle = Triangle()
circle = Circle()

print(f"Area of Square: {square.calculate_area(float(input('Side of Square: ')))}")
print(f"Area of Triangle: {triangle.calculate_area(float(input('Base of Triangle: ')), float(input('Height of Triangle: ')))}")
print(f"Area of Circle: {circle.calculate_area(float(input('Radius of Circle: ')))}")
