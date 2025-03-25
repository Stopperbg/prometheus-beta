import pytest
from src.even_odd_summary import summarize_numbers

def test_mixed_numbers():
    """Test with a mix of even and odd numbers."""
    result = summarize_numbers([1, 2, 3, 4, 5, 6])
    assert result == (12, 3)

def test_all_even_numbers():
    """Test with only even numbers."""
    result = summarize_numbers([2, 4, 6, 8])
    assert result == (20, 0)

def test_all_odd_numbers():
    """Test with only odd numbers."""
    result = summarize_numbers([1, 3, 5, 7])
    assert result == (0, 4)

def test_empty_list():
    """Test with an empty list."""
    result = summarize_numbers([])
    assert result == (0, 0)

def test_negative_numbers():
    """Test with negative numbers."""
    result = summarize_numbers([-1, -2, -3, -4, -5, -6])
    assert result == (-12, 3)

def test_mixed_negative_and_positive():
    """Test with mixed negative and positive numbers."""
    result = summarize_numbers([-1, 2, -3, 4, -5, 6])
    assert result == (12, 3)

def test_invalid_input_type():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        summarize_numbers("not a list")

def test_invalid_list_element_type():
    """Test raising TypeError for non-integer list elements."""
    with pytest.raises(TypeError, match="All elements in the list must be integers"):
        summarize_numbers([1, 2, "3", 4])

def test_zero_handling():
    """Test handling of zero."""
    result = summarize_numbers([0, 1, 2, 3])
    assert result == (2, 2)