import pytest
from src.bitonic_sort import bitonic_sort

def test_bitonic_sort_ascending():
    """Test ascending sort of a standard list"""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected = sorted(input_list)
    assert bitonic_sort(input_list) == expected

def test_bitonic_sort_descending():
    """Test descending sort of a standard list"""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected = sorted(input_list, reverse=True)
    assert bitonic_sort(input_list, ascending=False) == expected

def test_bitonic_sort_empty_list():
    """Test sorting an empty list"""
    assert bitonic_sort([]) == []

def test_bitonic_sort_single_element():
    """Test sorting a list with a single element"""
    input_list = [42]
    assert bitonic_sort(input_list) == input_list

def test_bitonic_sort_already_sorted():
    """Test sorting an already sorted list"""
    input_list = [1, 2, 3, 4, 5]
    assert bitonic_sort(input_list) == input_list

def test_bitonic_sort_reverse_sorted():
    """Test sorting a reverse-sorted list"""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert bitonic_sort(input_list) == expected

def test_bitonic_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    input_list = [4, 2, 2, 8, 3, 3, 1]
    expected = sorted(input_list)
    assert bitonic_sort(input_list) == expected

def test_bitonic_sort_invalid_input():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        bitonic_sort("not a list")

def test_bitonic_sort_consistent_original():
    """Ensure the original list is not modified"""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    original = input_list.copy()
    bitonic_sort(input_list)
    assert input_list == original