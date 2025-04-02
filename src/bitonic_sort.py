def bitonic_sort(arr, ascending=True):
    """
    Implement the bitonic sort algorithm.
    
    Bitonic sort is a comparison-based sorting algorithm that can sort sequences 
    in either ascending or descending order by recursively splitting the sequence 
    into bitonic sequences and merging them.
    
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
    
    def bitonic_merge(start, size, direction):
        """
        Merge a bitonic sequence
        
        Args:
            start (int): Starting index
            size (int): Number of elements to merge
            direction (bool): Sort direction 
        """
        if size > 1:
            k = size // 2
            
            # Compare and swap elements
            for i in range(start, start + k):
                if (direction and arr[i] > arr[i + k]) or \
                   (not direction and arr[i] < arr[i + k]):
                    arr[i], arr[i + k] = arr[i + k], arr[i]
            
            # Recursively merge subarrays
            bitonic_merge(start, k, direction)
            bitonic_merge(start + k, k, direction)
    
    def bitonic_sort_recursive(start, size, direction):
        """
        Recursively sort a sequence to create a bitonic sequence
        
        Args:
            start (int): Starting index
            size (int): Number of elements to sort
            direction (bool): Final sort direction
        """
        if size > 1:
            mid = size // 2
            
            # Sort first half ascending 
            bitonic_sort_recursive(start, mid, True)
            
            # Sort second half descending
            bitonic_sort_recursive(start + mid, size - mid, False)
            
            # Merge the entire sequence
            bitonic_merge(start, size, direction)
    
    # Start the recursive sorting process
    bitonic_sort_recursive(0, len(arr), ascending)
    
    return arr