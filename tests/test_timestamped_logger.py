import os
import tempfile
import pytest
import logging
from src.timestamped_logger import log_with_timestamp

@pytest.fixture
def temp_log_dir():
    """Create a temporary directory for log files"""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield tmpdir

def test_log_with_timestamp_default(temp_log_dir):
    """Test default logging functionality"""
    log_file = os.path.join(temp_log_dir, 'default.log')
    
    # Log a message
    result = log_with_timestamp("Test default log", log_file=log_file)
    
    # Check return value
    assert result is True
    
    # Verify log file was created and contains the message
    with open(log_file, 'r') as f:
        log_content = f.read()
        assert "Test default log" in log_content
        assert "INFO" in log_content

def test_log_with_timestamp_different_levels(temp_log_dir):
    """Test logging with different log levels"""
    levels = ['DEBUG', 'WARNING', 'ERROR', 'CRITICAL']
    
    for level in levels:
        log_file = os.path.join(temp_log_dir, f'test_{level.lower()}.log')
        
        # Log a message with specific level
        result = log_with_timestamp(f"Test {level} log", log_level=level, log_file=log_file)
        
        # Check return value
        assert result is True
        
        # Verify log file was created and contains the message
        with open(log_file, 'r') as f:
            log_content = f.read()
            assert f"Test {level} log" in log_content
            assert level in log_content

def test_log_invalid_level():
    """Test that an invalid log level raises a ValueError"""
    with pytest.raises(ValueError, match="Invalid log level"):
        log_with_timestamp("Test invalid log", log_level="INVALID")

def test_log_custom_file(temp_log_dir):
    """Test logging to a custom file in a subdirectory"""
    log_file = os.path.join(temp_log_dir, 'logs', 'custom_log.log')
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    
    # Log a message to custom file
    result = log_with_timestamp("Test custom log file", log_file=log_file)
    
    # Check return value
    assert result is True
    
    # Verify log file was created and contains the message
    with open(log_file, 'r') as f:
        log_content = f.read()
        assert "Test custom log file" in log_content
        assert "INFO" in log_content