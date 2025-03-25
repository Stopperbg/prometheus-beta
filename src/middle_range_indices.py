def find_middle_range_indices(sorted_list, range_radius=1):
    """
    Find indices of elements within a given range of the middle value in a sorted list.

    Args:
        sorted_list (list): A sorted list of integers
        range_radius (int, optional): Number of elements to include on each side of the middle. 
                                      Defaults to 1.

    Returns:
        list: Indices of elements within the specified range of the middle value

    Raises:
        ValueError: If the input list is empty
        TypeError: If inputs are not of the correct type
    """
    # Input validation
    if not isinstance(sorted_list, list):
        raise TypeError("Input must be a list")
    
    if not sorted_list:
        raise ValueError("Input list cannot be empty")
    
    if not isinstance(range_radius, int) or range_radius < 0:
        raise ValueError("Range radius must be a non-negative integer")
    
    # Determine the middle index
    list_length = len(sorted_list)
    
    # For odd-length lists, middle is the exact middle
    # For even-length lists, we'll use the left-of-center index
    middle_index = (list_length - 1) // 2
    
    # Calculate the start and end indices for the range
    start_index = max(0, middle_index - range_radius)
    end_index = min(list_length - 1, middle_index + range_radius)
    
    # Return the range of indices
    return list(range(start_index, end_index + 1))