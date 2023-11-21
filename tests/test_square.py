import pytest 
import src.shapes as shapes


def test_square_init_1():
    square = shapes.Square(3)
    assert square.area() == 9
    square = shapes.Square(5)
    assert square.area() == 25
    square = shapes.Square(4)
    assert square.area() == 16

def test_square_init_2():
    for (side_length, expected_area) in [(3,9),(5,25),(4,16)]:
        square = shapes.Square(side_length)
        assert square.area() == expected_area

@pytest.mark.parametrize('side_length, expected_area', [(3,9),(5,25),(4,16)])
def test_square_areas(side_length, expected_area):
    square = shapes.Square(side_length)
    assert square.area() == expected_area


@pytest.mark.parametrize('side_length, expected_perimeter', [(3,12),(5,20),(4,16)])
def test_square_perimeters(side_length, expected_perimeter):
    square = shapes.Square(side_length)
    assert square.perimeter() == expected_perimeter


