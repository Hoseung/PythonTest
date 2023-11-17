import math
import pytest 
import src.shapes as rectangle



def test_area():
    assert my_rectangle.area() == 2 * (my_rectangle.width * my_rectangle.height) 

def test_perimeter():
    assert my_rectangle.perimeter() == 2 * (my_rectangle.width + my_rectangle.height)



def test_not_equal(my_rectangle, weird_rectangle):
    assert my_rectangle != weird_rectangle