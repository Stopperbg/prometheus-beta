import pytest
from src.ip_validator import is_valid_ip_address

def test_valid_ip_addresses():
    """Test various valid IP addresses."""
    valid_ips = [
        '0.0.0.0',
        '255.255.255.255', 
        '192.168.0.1',
        '10.0.0.1',
        '172.16.0.1'
    ]
    
    for ip in valid_ips:
        assert is_valid_ip_address(ip) == True, f"{ip} should be valid"

def test_invalid_ip_addresses():
    """Test various invalid IP addresses."""
    invalid_ips = [
        # Out of range
        '256.0.0.1',
        '0.256.0.1',
        '0.0.256.1',
        '0.0.0.256',
        
        # Negative numbers
        '-1.0.0.0',
        '0.-1.0.0',
        '0.0.-1.0',
        '0.0.0.-1',
        
        # Extra/missing dots
        '1.2.3',
        '1.2.3.4.5',
        
        # Invalid formats
        'a.b.c.d',
        '192.168.0',
        '192.168.0.',
        '.192.168.0',
        
        # Leading zeros
        '01.02.03.04',
        '001.002.003.004',
        
        # Non-string inputs
        123,
        None,
        ['192.168.0.1']
    ]
    
    for ip in invalid_ips:
        assert is_valid_ip_address(ip) == False, f"{ip} should be invalid"

def test_edge_cases():
    """Test edge case IP addresses."""
    edge_cases = [
        # Boundary values
        '0.0.0.0',
        '255.255.255.255'
    ]
    
    for ip in edge_cases:
        assert is_valid_ip_address(ip) == True, f"{ip} should be valid"

def test_input_types():
    """Test various input types."""
    assert is_valid_ip_address(None) == False
    assert is_valid_ip_address(123) == False
    assert is_valid_ip_address([]) == False
    assert is_valid_ip_address({}) == False