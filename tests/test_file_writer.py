"""
Unit tests for the file_writer module.
"""

import os
import pytest
from src.file_writer import write_string_to_file

def test_write_string_to_file_basic():
    """Test basic file writing functionality."""
    test_path = 'tests/test_output.txt'
    test_content = "Hello, world!"
    
    # Write the file
    write_string_to_file(test_path, test_content)
    
    # Verify file contents
    with open(test_path, 'r') as file:
        assert file.read() == test_content
    
    # Clean up
    os.remove(test_path)

def test_write_string_to_file_empty_content():
    """Test writing an empty string to a file."""
    test_path = 'tests/test_empty.txt'
    test_content = ""
    
    # Write the file
    write_string_to_file(test_path, test_content)
    
    # Verify file contents
    with open(test_path, 'r') as file:
        assert file.read() == ""
    
    # Clean up
    os.remove(test_path)

def test_write_string_to_file_unicode():
    """Test writing unicode content to a file."""
    test_path = 'tests/test_unicode.txt'
    test_content = "こんにちは世界"  # Japanese: "Hello World"
    
    # Write the file
    write_string_to_file(test_path, test_content)
    
    # Verify file contents
    with open(test_path, 'r', encoding='utf-8') as file:
        assert file.read() == test_content
    
    # Clean up
    os.remove(test_path)

def test_write_string_to_file_invalid_path():
    """Test writing to an invalid file path."""
    with pytest.raises(IOError):
        write_string_to_file('/invalid/path/test.txt', "Some content")

def test_write_string_to_file_invalid_types():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        write_string_to_file(123, "Content")
    
    with pytest.raises(TypeError):
        write_string_to_file("test.txt", 456)

def test_write_string_to_file_empty_path():
    """Test error handling for empty file path."""
    with pytest.raises(ValueError):
        write_string_to_file("", "Content")
    
    with pytest.raises(ValueError):
        write_string_to_file("   ", "Content")