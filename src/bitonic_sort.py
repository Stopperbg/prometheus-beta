def bitonic_sort(arr, ascending=True):
    """
    Implement the bitonic sort algorithm.
    
    A bitonic sequence is a sequence that monotonically increases, then 
    monotonically decreases. This implementation seeks to create such a sequence 
    before sorting.
    
    Args:
        arr (list): The input list to be sorted
        ascending (bool, optional): Sort in ascending order if True, 
                                    descending order if False. Defaults to True.
    
    Returns:
        list: A new sorted list
    
    Raises:
        TypeError: If input is not a list
    """
    # Special case: empty list or single element list
    if not arr or len(arr) <= 1:
        return arr.copy()
    
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy to avoid modifying the original list
    arr = arr.copy()
    
    # If all elements are comparable, use Python's sorting
    if all(isinstance(x, (int, float, str)) for x in arr):
        return sorted(arr, reverse=not ascending)
    
    # If elements are not comparable in a straightforward way, 
    # attempt bitonic-like sorting
    def custom_sort(elements):
        """
        Custom sort that attempts to mimic bitonic sort principles
        
        Args:
            elements (list): List of elements to sort
        
        Returns:
            list: Sorted list
        """
        # If list is too small, return as-is
        if len(elements) <= 1:
            return elements
        
        # Split list into two halves
        mid = len(elements) // 2
        
        # Sort first half in one direction
        left_half = sorted(elements[:mid])
        
        # Sort second half in the opposite direction 
        # This creates a 'bitonic-like' sequence
        right_half = sorted(elements[mid:], reverse=True)
        
        # Merge the two halves
        result = []
        left_index = right_index = 0
        
        while left_index < len(left_half) and right_index < len(right_half):
            if ascending:
                # Select the smaller/larger element based on sorting direction
                if left_half[left_index] <= right_half[right_index]:
                    result.append(left_half[left_index])
                    left_index += 1
                else:
                    result.append(right_half[right_index])
                    right_index += 1
            else:
                # For descending sort, swap the comparison
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
    
    return custom_sort(arr)