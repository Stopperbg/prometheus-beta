def sum_of_multiples(min_val: int, max_val: int) -> int:
    """
    Calculate the sum of all multiples of 2 and 3 within an inclusive range.
    
    Args:
        min_val (int): The minimum value of the range (inclusive)
        max_val (int): The maximum value of the range (inclusive)
    
    Returns:
        int: The sum of all numbers in the range that are multiples of 2 or 3
    
    Raises:
        ValueError: If min_val is greater than max_val
    """
    # Validate input
    if min_val > max_val:
        raise ValueError("Minimum value must be less than or equal to maximum value")
    
    # Use a set to avoid duplicate counting
    multiples = set()
    
    # Find and add multiples of 2
    multiples.update(range(min_val if min_val % 2 == 0 else min_val + 1, 
                           max_val + 1, 2))
    
    # Find and add multiples of 3
    multiples.update(range(min_val if min_val % 3 == 0 else min_val + (3 - min_val % 3), 
                           max_val + 1, 3))
    
    return sum(multiples)