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
        ValueError: If list contains non-comparable elements
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy to avoid modifying the original list
    arr = arr.copy()
    
    def compare_and_swap(arr, i, j, direction):
        """
        Compare and potentially swap elements based on the direction
        
        Args:
            arr (list): The list to modify
            i (int): Index of first element
            j (int): Index of second element
            direction (bool): Sort direction
        """
        if (direction and arr[i] > arr[j]) or (not direction and arr[i] < arr[j]):
            arr[i], arr[j] = arr[j], arr[i]
    
    def bitonic_merge(arr, low, count, direction):
        """
        Merge a bitonic sequence
        
        Args:
            arr (list): The list to merge
            low (int): Starting index
            count (int): Number of elements to merge
            direction (bool): Sort direction
        """
        if count > 1:
            k = count // 2
            for i in range(low, low + k):
                compare_and_swap(arr, i, i + k, direction)
            
            bitonic_merge(arr, low, k, direction)
            bitonic_merge(arr, low + k, k, direction)
    
    def bitonic_sort_recursive(arr, low, count, direction):
        """
        Recursively sort a bitonic sequence
        
        Args:
            arr (list): The list to sort
            low (int): Starting index
            count (int): Number of elements to sort
            direction (bool): Sort direction
        """
        if count > 1:
            k = count // 2
            
            # Sort first half in ascending order
            bitonic_sort_recursive(arr, low, k, True)
            
            # Sort second half in descending order
            bitonic_sort_recursive(arr, low + k, k, False)
            
            # Merge entire sequence in the specified direction
            bitonic_merge(arr, low, count, direction)
    
    # Start the recursive sorting process
    bitonic_sort_recursive(arr, 0, len(arr), ascending)
    
    return arr