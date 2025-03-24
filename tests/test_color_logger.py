import pytest
import sys
import io
from src.color_logger import log_with_color

def test_log_with_color_default():
    """Test default logging without colors"""
    output = io.StringIO()
    log_with_color("Test message", file=output)
    result = output.getvalue().strip()
    assert result == "[INFO] Test message"

def test_log_with_text_color():
    """Test logging with a specific text color"""
    output = io.StringIO()
    log_with_color("Colored text", text_color="red", file=output)
    result = output.getvalue().strip()
    assert "[INFO] Colored text" in result
    
def test_log_with_background_color():
    """Test logging with a specific background color"""
    output = io.StringIO()
    log_with_color("Background colored", background_color="blue", file=output)
    result = output.getvalue().strip()
    assert "[INFO] Background colored" in result

def test_log_different_levels():
    """Test logging with different log levels"""
    levels = ['info', 'warning', 'error', 'debug']
    for level in levels:
        output = io.StringIO()
        log_with_color(f"Test {level}", level=level, file=output)
        result = output.getvalue().strip()
        assert result.startswith(f"[{level.upper()}] Test {level}")

def test_invalid_text_color():
    """Test that an invalid text color raises a ValueError"""
    with pytest.raises(ValueError, match="Invalid text color"):
        log_with_color("Test", text_color="invalid_color")

def test_invalid_background_color():
    """Test that an invalid background color raises a ValueError"""
    with pytest.raises(ValueError, match="Invalid background color"):
        log_with_color("Test", background_color="invalid_color")

def test_invalid_log_level():
    """Test that an invalid log level raises a ValueError"""
    with pytest.raises(ValueError, match="Invalid log level"):
        log_with_color("Test", level="invalid_level")

def test_color_and_level_combination():
    """Test logging with both color and log level"""
    output = io.StringIO()
    log_with_color("Complex log", 
                   text_color="green", 
                   background_color="yellow", 
                   level="warning", 
                   file=output)
    result = output.getvalue().strip()
    assert "[WARNING] Complex log" in result