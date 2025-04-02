def bitonic_sort(arr, ascending=True):
    """
    Implement the bitonic sort algorithm.
    
    Bitonic sort is a comparison-based sorting algorithm that can sort sequences 
    in either ascending or descending order.
    
    Args:
        arr (list): The input list to be sorted
        ascending (bool, optional): Sort in ascending order if True, 
                                    descending order if False. Defaults to True.
    
    Returns:
        list: A new sorted list
    
    Raises:
        TypeError: If input is not a list
    """
    # Special case: empty list
    if not arr:
        return []
    
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy to avoid modifying the original list
    arr = arr.copy()
    
    # If the list is small, use built-in sorting
    if len(arr) <= 1:
        return arr
    
    # Split the list into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort each half 
    # First half ascending, second half descending
    left_half.sort()
    right_half.sort(reverse=True)
    
    # Merge the sorted halves
    result = []
    left_index = right_index = 0
    
    while left_index < len(left_half) and right_index < len(right_half):
        if ascending:
            # Ascending sort: pick the smaller element
            if left_half[left_index] <= right_half[right_index]:
                result.append(left_half[left_index])
                left_index += 1
            else:
                result.append(right_half[right_index])
                right_index += 1
        else:
            # Descending sort: pick the larger element
            if left_half[left_index] >= right_half[right_index]:
                result.append(left_half[left_index])
                left_index += 1
            else:
                result.append(right_half[right_index])
                right_index += 1
    
    # Add remaining elements
    result.extend(left_half[left_index:])
    result.extend(right_half[right_index:])
    
    return result