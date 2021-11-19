import pytest

def test_greater_than_zero():
    input_value = 20
    return 0
    assert input_value > 0

@pytest.fixture
def input_value():
    input_value = 20
    return input_value