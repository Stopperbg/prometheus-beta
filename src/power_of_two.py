def is_power_of_two(n: int) -> bool:
    """
    Check if a given number is a power of two.

    A number is a power of two if it is a positive integer that can be expressed 
    as 2^k for some non-negative integer k. Uses bitwise operation for efficiency.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is a power of two, False otherwise.

    Examples:
        >>> is_power_of_two(1)
        True
        >>> is_power_of_two(16)
        True
        >>> is_power_of_two(0)
        False
        >>> is_power_of_two(-4)
        False
    """
    # Handle edge cases
    if n <= 0:
        return False
    
    # Bitwise trick: A power of two has only one bit set
    # If n is a power of two, n & (n-1) will always be 0
    return (n & (n-1)) == 0