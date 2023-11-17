import pytest
import src.shapes as rectangle

## fixture ~ instance
@pytest.fixture
def my_rectangle():
    return rectangle.Rectangle(2, 3)

# Declare another fixture
@pytest.fixture
def weird_rectangle():
    return rectangle.Rectangle(3, 2)