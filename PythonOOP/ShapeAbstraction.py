class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


rectangle = Rectangle(5, 4)
print(f"Area of rectangle is: {rectangle.area()}")

circle = Circle(5)
print(f"Area of Circle is: {circle.area()}")
print("make sure to add the right comments")