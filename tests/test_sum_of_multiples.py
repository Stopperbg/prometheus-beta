import pytest
from src.sum_of_multiples import sum_of_multiples

def test_sum_of_multiples_basic_range():
    """Test basic range with multiples of 2 and 3"""
    result = sum_of_multiples(1, 10)
    print(f"Basic range result: {result}")
    assert result == 33  # 2 + 3 + 4 + 6 + 8 + 9 + 10

def test_sum_of_multiples_zero_range():
    """Test range starting at zero"""
    result = sum_of_multiples(0, 10)
    print(f"Zero range result: {result}")
    assert result == 33

def test_sum_of_multiples_single_number():
    """Test range with a single number"""
    assert sum_of_multiples(6, 6) == 6
    assert sum_of_multiples(5, 5) == 0

def test_sum_of_multiples_large_range():
    """Test a larger range"""
    result = sum_of_multiples(1, 100)
    print(f"Large range result: {result}")
    assert result == 2418

def test_sum_of_multiples_invalid_range():
    """Test invalid range where min > max"""
    with pytest.raises(ValueError, match="Minimum value must be less than or equal to maximum value"):
        sum_of_multiples(10, 1)

def test_sum_of_multiples_edge_cases():
    """Test edge cases"""
    result = sum_of_multiples(-10, 10)
    print(f"Edge case result: {result}")
    assert result == 33
    assert sum_of_multiples(-20, -10) == -30