import math
import pytest 
import src.shapes as rectangle

## fixture ~ instance

@pytest.fixture
def my_rectangle():
    return rectangle.Rectangle(2, 3)

def test_area():
    assert my_rectangle.area() == 2 * (my_rectangle.width * my_rectangle.height) 

def test_perimeter():
    assert my_rectangle.perimeter() == 2 * (my_rectangle.width + my_rectangle.height)

# Declare another fixture
@pytest.fixture
def weird_rectangle():
    return rectangle.Rectangle(3, 2)


def test_not_equal(my_rectangle, weird_rectangle):
    assert my_rectangle != weird_rectangle