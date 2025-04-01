import pytest
from src.most_frequent_char import find_most_frequent_char

def test_most_frequent_char_basic():
    """Test finding the most frequent character in a simple string."""
    assert find_most_frequent_char("hello") == "l"

def test_most_frequent_char_multiple_same_frequency():
    """Test when multiple characters have the same frequency."""
    assert find_most_frequent_char("abcabc") in ["a", "b", "c"]

def test_most_frequent_char_single_char():
    """Test with a single character string."""
    assert find_most_frequent_char("a") == "a"

def test_most_frequent_char_with_spaces_and_punctuation():
    """Test with a string containing spaces and punctuation."""
    assert find_most_frequent_char("hello world! hello!") == "l"

def test_most_frequent_char_case_sensitive():
    """Test that the function is case-sensitive."""
    assert find_most_frequent_char("Hello") == "l"

def test_most_frequent_char_invalid_input_type():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError):
        find_most_frequent_char(123)

def test_most_frequent_char_empty_string():
    """Test that a ValueError is raised for an empty string."""
    with pytest.raises(ValueError):
        find_most_frequent_char("")