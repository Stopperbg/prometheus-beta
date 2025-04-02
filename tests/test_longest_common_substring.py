import pytest
from src.longest_common_substring import find_longest_common_substring

def test_basic_common_substring():
    """Test basic scenario with a common substring"""
    assert find_longest_common_substring("hello", "help") == "hel"
    assert find_longest_common_substring("programming", "program") == "program"

def test_no_common_substring():
    """Test when no common substring exists"""
    assert find_longest_common_substring("abc", "xyz") == ""

def test_empty_strings():
    """Test scenarios with empty strings"""
    assert find_longest_common_substring("", "hello") == ""
    assert find_longest_common_substring("world", "") == ""
    assert find_longest_common_substring("", "") == ""

def test_identical_strings():
    """Test when strings are identical"""
    assert find_longest_common_substring("python", "python") == "python"

def test_case_sensitivity():
    """Test case sensitivity of the function"""
    assert find_longest_common_substring("Python", "python") == ""

def test_substring_at_different_positions():
    """Test common substring at different positions"""
    assert find_longest_common_substring("abcdef", "bcdefg") == "bcdef"
    assert find_longest_common_substring("xabcx", "yabcy") == "abc"

def test_multiple_possible_substrings():
    """Test when multiple common substrings exist"""
    assert find_longest_common_substring("abcabc", "bcabca") == "bcab"

def test_long_strings():
    """Test with longer input strings"""
    s1 = "abcdefghijklmnopqrstuvwxyz"
    s2 = "mnopqrstuvwxyzabcdefghijkl"
    assert find_longest_common_substring(s1, s2) == "mnopqrstuvwxyz"