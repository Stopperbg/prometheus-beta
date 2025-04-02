def is_valid_ip_address(ip_string):
    """
    Check if a given string is a valid IPv4 address.
    
    Args:
        ip_string (str): The string to validate as an IP address.
    
    Returns:
        bool: True if the string is a valid IPv4 address, False otherwise.
    
    Examples:
        >>> is_valid_ip_address('192.168.0.1')
        True
        >>> is_valid_ip_address('255.255.255.255')
        True
        >>> is_valid_ip_address('0.0.0.0')
        True
        >>> is_valid_ip_address('256.0.0.1')
        False
        >>> is_valid_ip_address('1.2.3.4.5')
        False
        >>> is_valid_ip_address('192.168.0')
        False
    """
    # Check if the input is a string
    if not isinstance(ip_string, str):
        return False
    
    # Split the string into octets
    octets = ip_string.split('.')
    
    # Check if there are exactly 4 octets
    if len(octets) != 4:
        return False
    
    # Check each octet
    for octet in octets:
        # Check if octet is a valid integer string
        try:
            # Convert to integer and check range
            num = int(octet)
            
            # Check for leading zeros (except for 0 itself)
            if len(octet) > 1 and octet[0] == '0':
                return False
            
            # Check range (0-255)
            if num < 0 or num > 255:
                return False
        
        except ValueError:
            # Not a valid integer
            return False
    
    return True