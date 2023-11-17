import math
import pytest 
import time

def test_area(my_rectangle):
    assert my_rectangle.area() == 2 * (my_rectangle.width * my_rectangle.height) 

def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == 2 * (my_rectangle.width + my_rectangle.height)

def test_not_equal(my_rectangle, weird_rectangle):
    assert my_rectangle != weird_rectangle

@pytest.mark.slow
def test_slow():
    time.sleep(5)
    assert True

@pytest.mark.skip(reason="I don't want to run this test right now.")
def test_skip():
    assert False

@pytest.mark.xfail(reason="I know this test will fail.")
def test_xfail():
    assert False