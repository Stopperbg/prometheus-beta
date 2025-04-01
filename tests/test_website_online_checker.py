import pytest
from src.website_online_checker import is_website_online

def test_valid_website_online():
    """Test a known online website."""
    result, message = is_website_online('www.google.com')
    assert result is True
    assert 'is online' in message

def test_invalid_url():
    """Test handling of invalid URL."""
    result, message = is_website_online('')
    assert result is False
    assert 'Invalid URL' in message

def test_non_existent_website():
    """Test a non-existent website."""
    result, message = is_website_online('www.thissitedoesnotexist123456789.com', timeout=2)
    assert result is False
    assert 'Connection error' in message

def test_timeout_website():
    """Test website connection timeout."""
    result, message = is_website_online('www.veryslowtimeoutsite.com', timeout=1)
    assert result is False
    assert 'timed out' in message

def test_https_handling():
    """Test that URLs without protocol are handled."""
    result, message = is_website_online('google.com')
    assert result is True
    assert 'is online' in message