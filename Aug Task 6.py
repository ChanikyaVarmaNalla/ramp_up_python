import math

class Shape:
    def calculate_area(self):
        pass

class Square(Shape):
    def calculate_area(self):
        side = float(input("Enter the side length of the square: "))
        if side < 0:
            print(f"Negative side length ({side}) is not valid. Please provide a valid positive value.")
            return self.calculate_area()
        print(f"{self.__class__.__name__} (Child) calculates the area.")
        return side ** 2

class Triangle(Shape):
    def calculate_area(self):
        base = float(input("Enter the base length of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        if base < 0 or height < 0:
            print(f"Negative base ({base}) or height ({height}) is not valid. Please provide valid positive values.")
            return self.calculate_area()
        print(f"{self.__class__.__name__} (Child) calculates the area.")
        return 0.5 * base * height

class Circle(Shape):
    def calculate_area(self):
        radius = float(input("Enter the radius of the circle: "))
        if radius < 0:
            print(f"Negative radius ({radius}) is not valid. Please provide a valid positive value.")
            return self.calculate_area()
        print(f"{self.__class__.__name__} (Child) calculates the area.")
        return math.pi * radius ** 2

def calculate_shape_area(shape_choice):
    if shape_choice == '1':
        square = Square()
        return square.calculate_area()
    elif shape_choice == '2':
        triangle = Triangle()
        return triangle.calculate_area()
    elif shape_choice == '3':
        circle = Circle()
        return circle.calculate_area()
    else:
        print("Invalid choice. Please select a valid option.")
        return None

print("Welcome to the Area Calculator!")

while True:
    print("\nSelect a shape to calculate its area:")
    print("1. Square")
    print("2. Triangle")
    print("3. Circle")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '4':
        print("Thank you for using the Area Calculator. Goodbye!")
        break

    area = calculate_shape_area(choice)
    if area is not None:
        print(f"Area: {area}")
