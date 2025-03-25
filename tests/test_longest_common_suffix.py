import pytest
from src.longest_common_suffix import find_longest_common_suffix

def test_basic_common_suffix():
    """Test finding a basic common suffix"""
    assert find_longest_common_suffix(["flower", "power", "tower"]) == "ower"

def test_single_string():
    """Test with a single string"""
    assert find_longest_common_suffix(["hello"]) == "hello"

def test_empty_list():
    """Test with an empty list"""
    assert find_longest_common_suffix([]) == ""

def test_no_common_suffix():
    """Test when no common suffix exists"""
    assert find_longest_common_suffix(["abc", "def", "ghi"]) == ""

def test_full_common_suffix():
    """Test when all strings are identical"""
    assert find_longest_common_suffix(["hello", "hello", "hello"]) == "hello"

def test_partial_common_suffix():
    """Test with partial common suffix"""
    assert find_longest_common_suffix(["window", "snow", "glow"]) == "ow"

def test_single_character_suffix():
    """Test with single character suffix"""
    assert find_longest_common_suffix(["cat", "bat", "rat"]) == "at"

def test_invalid_input_not_list():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list of strings"):
        find_longest_common_suffix("not a list")

def test_invalid_input_non_string_elements():
    """Test raising TypeError for list with non-string elements"""
    with pytest.raises(TypeError, match="All elements must be strings"):
        find_longest_common_suffix(["string", 123, "another"])

def test_mixed_case_suffix():
    """Test common suffix with mixed case sensitivity"""
    assert find_longest_common_suffix(["Hello", "hello"]) == ""