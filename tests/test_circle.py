import math
import pytest
import src.shapes as circle

class Teset_circle():

    def setup_method(self, method):
        print(f"setting up {method.__name__}")
        self.circle = circle.Circle(2)

    def test_area(self):
        assert self.circle.area() == self.circle**2 * math.pi

    def test_perimeter(self):
        assert self.circle.perimeter() == 2 * math.pi * self.circle.radius


def test_circle():
    cc = circle.Circle(2)
    assert cc.radius == 2
    assert cc.area() == 2**2 * math.pi
    assert cc.perimeter() == 2 * math.pi * cc.radius