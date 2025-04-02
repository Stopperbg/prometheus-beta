import pytest
from src.bubble_sort import bubble_sort

def test_bubble_sort_basic():
    """Test basic sorting of integers."""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected = [11, 12, 22, 25, 34, 64, 90]
    assert bubble_sort(input_list) == expected

def test_bubble_sort_already_sorted():
    """Test sorting a list that is already sorted."""
    input_list = [1, 2, 3, 4, 5]
    assert bubble_sort(input_list) == input_list

def test_bubble_sort_reverse_sorted():
    """Test sorting a list in reverse order."""
    input_list = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert bubble_sort(input_list) == expected

def test_bubble_sort_empty_list():
    """Test sorting an empty list."""
    assert bubble_sort([]) == []

def test_bubble_sort_single_element():
    """Test sorting a list with a single element."""
    input_list = [42]
    assert bubble_sort(input_list) == input_list

def test_bubble_sort_duplicate_elements():
    """Test sorting a list with duplicate elements."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    assert bubble_sort(input_list) == expected

def test_bubble_sort_floating_point():
    """Test sorting floating-point numbers."""
    input_list = [3.14, 2.71, 1.41, 0.58, 2.23]
    expected = [0.58, 1.41, 2.23, 2.71, 3.14]
    assert bubble_sort(input_list) == expected

def test_bubble_sort_strings():
    """Test sorting strings."""
    input_list = ['banana', 'apple', 'cherry', 'date']
    expected = ['apple', 'banana', 'cherry', 'date']
    assert bubble_sort(input_list) == expected

def test_bubble_sort_non_list_input():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        bubble_sort("not a list")

def test_bubble_sort_uncomparable_elements():
    """Test that a TypeError is raised for elements that cannot be compared."""
    with pytest.raises(TypeError, match="List contains elements that cannot be compared"):
        bubble_sort([1, 2, "3", [4]])