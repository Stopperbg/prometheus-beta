import pytest
from src.power_of_two import is_power_of_two

def test_is_power_of_two():
    """
    Test cases for is_power_of_two function covering various scenarios.
    """
    # Positive test cases (powers of two)
    assert is_power_of_two(1) == True
    assert is_power_of_two(2) == True
    assert is_power_of_two(4) == True
    assert is_power_of_two(8) == True
    assert is_power_of_two(16) == True
    assert is_power_of_two(1024) == True
    assert is_power_of_two(2**20) == True

    # Negative test cases (not powers of two)
    assert is_power_of_two(0) == False
    assert is_power_of_two(-1) == False
    assert is_power_of_two(-4) == False
    assert is_power_of_two(3) == False
    assert is_power_of_two(5) == False
    assert is_power_of_two(6) == False
    assert is_power_of_two(7) == False
    assert is_power_of_two(9) == False
    assert is_power_of_two(15) == False
    assert is_power_of_two(17) == False

def test_is_power_of_two_large_numbers():
    """
    Test large power of two numbers to ensure correct handling.
    """
    assert is_power_of_two(2**30) == True  # Large power of two
    assert is_power_of_two(2**31 - 1) == False  # Large number not a power of two

def test_is_power_of_two_type_errors():
    """
    Test handling of non-integer inputs.
    """
    with pytest.raises(TypeError):
        is_power_of_two(3.14)
    with pytest.raises(TypeError):
        is_power_of_two("16")
    with pytest.raises(TypeError):
        is_power_of_two(None)