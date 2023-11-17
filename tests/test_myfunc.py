import pytest
import src.myfunc as myfunc

def test_add():
    assert myfunc.add(7, 3) == 10
    assert myfunc.add(5, 2) == 7 

def test_add_strings():
    result = myfunc.add('Hello', ' World')
    assert result == 'Hello World'
    assert type(result) is str
    assert 'Heldlo' not in result

def test_divide():
    assert myfunc.divide(10, 5) == 2
    assert myfunc.divide(10, 2) == 5
    with pytest.raises(ZeroDivisionError):
        myfunc.divide(10, 0)
