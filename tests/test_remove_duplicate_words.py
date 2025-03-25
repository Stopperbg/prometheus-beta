import pytest
from src.remove_duplicate_words import remove_duplicate_words

def test_remove_duplicate_words_basic():
    """Test basic functionality of removing duplicate words."""
    assert remove_duplicate_words("hello world hello python world") == "hello world python"

def test_remove_duplicate_words_no_duplicates():
    """Test a string with no duplicate words."""
    assert remove_duplicate_words("one two three") == "one two three"

def test_remove_duplicate_words_all_duplicates():
    """Test a string with all duplicate words."""
    assert remove_duplicate_words("a a a a a") == "a"

def test_remove_duplicate_words_empty_string():
    """Test handling of an empty string."""
    assert remove_duplicate_words("") == ""

def test_remove_duplicate_words_whitespace():
    """Test handling of extra whitespace."""
    assert remove_duplicate_words("  hello   world  hello  ") == "hello world"

def test_remove_duplicate_words_invalid_input():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        remove_duplicate_words(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        remove_duplicate_words(None)

def test_remove_duplicate_words_order_preservation():
    """Test that the order of first occurrences is maintained."""
    assert remove_duplicate_words("python java python rust java go") == "python java rust go"