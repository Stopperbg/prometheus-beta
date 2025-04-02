def bitonic_sort(arr, ascending=True):
    """
    Implement the bitonic sort algorithm.
    
    Bitonic sort is a comparison-based sorting algorithm that can sort sequences 
    in either ascending or descending order by recursive bitonic splitting and merging.
    
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
    
    def bitonic_merge(arr, low, count, direction):
        """
        Merge a bitonic sequence
        
        Args:
            arr (list): The list to merge
            low (int): Starting index
            count (int): Number of elements to merge
            direction (bool): Sort direction 
        """
        if count <= 1:
            return
        
        # Find greatest power of 2 less than or equal to count
        step = 1
        while step < count:
            step *= 2
        step //= 2
        
        # Perform comparisons and swaps
        for i in range(low, low + count - step):
            # Perform comparison based on the sort direction
            if (direction and arr[i] > arr[i + step]) or \
               (not direction and arr[i] < arr[i + step]):
                arr[i], arr[i + step] = arr[i + step], arr[i]
        
        # Recursively merge subarrays
        if step > 1:
            bitonic_merge(arr, low, step, direction)
            bitonic_merge(arr, low + step, count - step, direction)
    
    def bitonic_convert(arr, ascending):
        """
        Convert input list to a bitonic sequence
        
        Args:
            arr (list): Input list
            ascending (bool): Desired sorting direction
        """
        # Pad to power of 2 to ensure consistent behavior
        n = 1
        while n < len(arr):
            n *= 2
        
        # Extend the list with copies to make it exactly a power of 2
        while len(arr) < n:
            arr.append(float('inf') if ascending else float('-inf'))
        
        # High-level bitonic split
        for length in range(2, n+1):
            for i in range(0, n, length):
                mid = length // 2
                
                # Bitonic split both subarrays
                for j in range(i, i + mid):
                    # Compare and swap based on direction
                    if (ascending and arr[j] > arr[j + mid]) or \
                       (not ascending and arr[j] < arr[j + mid]):
                        arr[j], arr[j + mid] = arr[j + mid], arr[j]
        
        return arr
    
    # Perform the bitonic sort
    if len(arr) > 1:
        arr = bitonic_convert(arr, ascending)
        bitonic_merge(arr, 0, len(arr), ascending)
    
    # Remove any padding and return
    return arr[:len(arr)]