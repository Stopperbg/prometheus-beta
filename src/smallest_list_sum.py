def find_smallest_sum(list1, list2):
    """
    Find the smallest possible sum between two lists of integers.
    
    Args:
        list1 (list): First list of integers
        list2 (list): Second list of integers
    
    Returns:
        int: The smallest possible sum that can be created by 
             combining one element from each list
    
    Raises:
        ValueError: If either input is not a list or is empty
    """
    # Validate input
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Inputs must be lists")
    
    if not list1 or not list2:
        raise ValueError("Lists cannot be empty")
    
    # Find the smallest possible sum
    smallest_sum = float('inf')
    
    for num1 in list1:
        for num2 in list2:
            current_sum = num1 + num2
            smallest_sum = min(smallest_sum, current_sum)
    
    return smallest_sum