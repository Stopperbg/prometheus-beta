import pytest
from src.log_bold import log_bold

def test_log_bold_normal_string():
    """Test logging a normal string in bold."""
    result = log_bold("Hello, World!")
    assert result == "\033[1mHello, World!\033[0m"

def test_log_bold_empty_string():
    """Test logging an empty string."""
    result = log_bold("")
    assert result == "\033[1m\033[0m"

def test_log_bold_with_special_characters():
    """Test logging a string with special characters."""
    result = log_bold("Hello, @#$%^&*()!")
    assert result == "\033[1mHello, @#$%^&*()!\033[0m"

def test_log_bold_with_numbers():
    """Test logging a string with numbers."""
    result = log_bold("42 is the answer")
    assert result == "\033[1m42 is the answer\033[0m"

def test_log_bold_raises_TypeError():
    """Test that TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        log_bold(42)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        log_bold(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        log_bold(["not", "a", "string"])