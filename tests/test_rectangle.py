import math
import pytest 


def test_area(my_rectangle):
    assert my_rectangle.area() == 2 * (my_rectangle.width * my_rectangle.height) 

def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == 2 * (my_rectangle.width + my_rectangle.height)



def test_not_equal(my_rectangle, weird_rectangle):
    assert my_rectangle != weird_rectangle