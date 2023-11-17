import math 

class Shape():
    def area(self):
        pass 

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius    
    

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        return False

    def area(self):
        return 2 * (self.width * self.height)

    def perimeter(self):
        return 2 * (self.width + self.height)