import pytest
import src.myfunc as myfunc

def test_add():
    assert myfunc.add(7, 3) == 10
    assert myfunc.add(7) == 9
    assert myfunc.add(5) == 7 


def test_divide():
    assert myfunc.divide(10, 5) == 2
    assert myfunc.divide(10, 2) == 5
    assert myfunc.divide(10) == 5
    with pytest.raises(TypeError):
        myfunc.divide(10, 0)
