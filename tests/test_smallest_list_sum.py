import pytest
from src.smallest_list_sum import find_smallest_sum

def test_basic_smallest_sum():
    """Test finding smallest sum with basic lists"""
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    assert find_smallest_sum(list1, list2) == 5  # 1 + 4

def test_negative_numbers():
    """Test finding smallest sum with negative numbers"""
    list1 = [-1, -2, -3]
    list2 = [-4, -5, -6]
    assert find_smallest_sum(list1, list2) == -7  # -3 + -4

def test_mixed_numbers():
    """Test finding smallest sum with mixed positive and negative numbers"""
    list1 = [-1, 2, 3]
    list2 = [4, -5, 6]
    assert find_smallest_sum(list1, list2) == -6  # -1 + -5

def test_single_element_lists():
    """Test with single-element lists"""
    list1 = [10]
    list2 = [5]
    assert find_smallest_sum(list1, list2) == 15  # 10 + 5

def test_empty_list_raises_error():
    """Test that empty lists raise a ValueError"""
    with pytest.raises(ValueError, match="Lists cannot be empty"):
        find_smallest_sum([], [1, 2, 3])
    
    with pytest.raises(ValueError, match="Lists cannot be empty"):
        find_smallest_sum([1, 2, 3], [])

def test_non_list_input_raises_error():
    """Test that non-list inputs raise a ValueError"""
    with pytest.raises(ValueError, match="Inputs must be lists"):
        find_smallest_sum("not a list", [1, 2, 3])
    
    with pytest.raises(ValueError, match="Inputs must be lists"):
        find_smallest_sum([1, 2, 3], "not a list")
    
    with pytest.raises(ValueError, match="Inputs must be lists"):
        find_smallest_sum(123, 456)