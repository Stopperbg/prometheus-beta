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
    
    # Use a set to avoid double-counting numbers that are multiples of both 2 and 3
    multiples = set()
    
    # Find multiples of 2
    for num in range(min_val, max_val + 1):
        if num % 2 == 0:
            multiples.add(num)
    
    # Find multiples of 3
    for num in range(min_val, max_val + 1):
        if num % 3 == 0:
            multiples.add(num)
    
    # Return the sum of unique multiples
    return sum(multiples)