import pytest
from src.find_first_last_occurrence import find_first_last_occurrence

def test_find_first_last_occurrence_normal_case():
    """Test finding first and last occurrence in a normal sorted array"""
    arr = [1, 2, 2, 2, 3, 4, 4, 5]
    assert find_first_last_occurrence(arr, 2) == (1, 3)
    assert find_first_last_occurrence(arr, 4) == (5, 6)

def test_find_first_last_occurrence_single_element():
    """Test when the target appears only once"""
    arr = [1, 2, 3, 4, 5]
    assert find_first_last_occurrence(arr, 3) == (2, 2)

def test_find_first_last_occurrence_element_not_found():
    """Test when the target is not in the array"""
    arr = [1, 2, 3, 4, 5]
    assert find_first_last_occurrence(arr, 6) == (-1, -1)
    assert find_first_last_occurrence(arr, 0) == (-1, -1)

def test_find_first_last_occurrence_empty_array():
    """Test with an empty array"""
    arr = []
    assert find_first_last_occurrence(arr, 1) == (-1, -1)

def test_find_first_last_occurrence_all_same_elements():
    """Test when all elements are the same"""
    arr = [2, 2, 2, 2, 2]
    assert find_first_last_occurrence(arr, 2) == (0, 4)

def test_find_first_last_occurrence_first_last_elements():
    """Test finding first and last elements of the array"""
    arr = [1, 1, 2, 3, 4, 5, 5, 5]
    assert find_first_last_occurrence(arr, 1) == (0, 1)
    assert find_first_last_occurrence(arr, 5) == (5, 7)