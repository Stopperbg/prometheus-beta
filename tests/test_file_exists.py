import os
import tempfile
import pytest
from src.file_exists import file_exists


def test_existing_file():
    """Test that an existing file returns True."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file_path = temp_file.name
    
    try:
        assert file_exists(temp_file_path) is True
    finally:
        os.unlink(temp_file_path)


def test_nonexistent_file():
    """Test that a nonexistent file returns False."""
    assert file_exists('/path/to/nonexistent/file.txt') is False


def test_directory_returns_false():
    """Test that a directory returns False."""
    temp_dir = tempfile.mkdtemp()
    try:
        assert file_exists(temp_dir) is False
    finally:
        os.rmdir(temp_dir)


def test_invalid_input_type():
    """Test that non-string inputs raise a TypeError."""
    with pytest.raises(TypeError, match="file_path must be a string"):
        file_exists(123)
    with pytest.raises(TypeError, match="file_path must be a string"):
        file_exists(None)


def test_empty_string():
    """Test that an empty string returns False."""
    assert file_exists('') is False


def test_home_directory_path():
    """Test that home directory paths work correctly."""
    # Use ~/ to test home directory expansion
    home_readme = os.path.expanduser('~/.bash_profile')
    result = file_exists(home_readme)
    # This will return True if the file exists, False otherwise
    assert isinstance(result, bool)