import pytest
from src.middle_range_indices import find_middle_range_indices

def test_odd_length_list_default_radius():
    """Test with an odd-length list and default range radius"""
    test_list = [1, 2, 3, 4, 5]
    result = find_middle_range_indices(test_list)
    assert result == [1, 2, 3]

def test_even_length_list_default_radius():
    """Test with an even-length list and default range radius"""
    test_list = [1, 2, 3, 4, 5, 6]
    result = find_middle_range_indices(test_list)
    assert result == [2, 3]

def test_custom_range_radius():
    """Test with a custom range radius"""
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = find_middle_range_indices(test_list, range_radius=2)
    assert result == [3, 4, 5]

def test_zero_range_radius():
    """Test with zero range radius"""
    test_list = [1, 2, 3, 4, 5]
    result = find_middle_range_indices(test_list, range_radius=0)
    assert result == [2]

def test_small_list():
    """Test with a very small list"""
    test_list = [42]
    result = find_middle_range_indices(test_list)
    assert result == [0]

def test_empty_list_raises_error():
    """Test that an empty list raises a ValueError"""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_middle_range_indices([])

def test_invalid_input_type():
    """Test that non-list input raises a TypeError"""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_middle_range_indices("not a list")

def test_invalid_range_radius():
    """Test that invalid range radius raises a ValueError"""
    with pytest.raises(ValueError, match="Range radius must be a non-negative integer"):
        find_middle_range_indices([1, 2, 3], range_radius=-1)

def test_large_range_radius():
    """Test with a large range radius that exceeds list bounds"""
    test_list = [1, 2, 3, 4, 5]
    result = find_middle_range_indices(test_list, range_radius=10)
    assert result == [0, 1, 2, 3, 4]