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
    
    def bitonic_sort_recursive(arr, low, count, direction):
        """
        Recursively sort a bitonic sequence
        
        Args:
            arr (list): The list to sort
            low (int): Starting index
            count (int): Number of elements to sort
            direction (bool): Sort direction
        """
        # Base case: if count is 1 or less, it's already sorted
        if count <= 1:
            return
        
        # Determine the middle point 
        mid = count // 2
        
        # Sort first half ascending
        bitonic_sort_recursive(arr, low, mid, True)
        
        # Sort second half descending 
        bitonic_sort_recursive(arr, low + mid, count - mid, False)
        
        # Merge the two halves
        bitonic_merge(arr, low, count, direction)
    
    def bitonic_merge(arr, low, count, direction):
        """
        Merge a bitonic sequence
        
        Args:
            arr (list): The list to merge
            low (int): Starting index
            count (int): Number of elements to merge
            direction (bool): Sort direction (True for ascending, False for descending)
        """
        # Base case
        if count <= 1:
            return
        
        # Find the greatest power of 2 less than or equal to count
        k = largest_power_of_two(count)
        
        # Perform comparison and swap
        for i in range(low, low + count - k):
            compare_and_swap(arr, i, i + k, direction)
        
        # Recursively merge the two halves
        bitonic_merge(arr, low, k, direction)
        bitonic_merge(arr, low + k, count - k, direction)
    
    def compare_and_swap(arr, i, j, direction):
        """
        Compare and potentially swap elements based on the direction
        
        Args:
            arr (list): The list to modify
            i (int): Index of first element
            j (int): Index of second element
            direction (bool): True for ascending, False for descending
        """
        if (direction and arr[i] > arr[j]) or (not direction and arr[i] < arr[j]):
            arr[i], arr[j] = arr[j], arr[i]
    
    def largest_power_of_two(n):
        """
        Find the largest power of 2 less than or equal to n
        
        Args:
            n (int): Input number
        
        Returns:
            int: Largest power of 2 less than or equal to n
        """
        power = 1
        while power * 2 <= n:
            power *= 2
        return power
    
    # Start the recursive sorting process
    bitonic_sort_recursive(arr, 0, len(arr), ascending)
    
    return arr