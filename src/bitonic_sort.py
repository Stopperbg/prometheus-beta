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
            direction (bool): Sort direction (True for ascending, False for descending)
        """
        if count <= 1:
            return
        
        # Compute the distance between elements to compare
        distance = count // 2
        
        # Compare and swap if needed
        for i in range(low, low + count - distance):
            if (direction and arr[i] > arr[i + distance]) or \
               (not direction and arr[i] < arr[i + distance]):
                arr[i], arr[i + distance] = arr[i + distance], arr[i]
        
        # Recursively merge subarrays
        if distance > 1:
            bitonic_merge(arr, low, distance, direction)
            bitonic_merge(arr, low + distance, distance, direction)
    
    def convert_to_bitonic(arr, ascending):
        """
        Convert input list to a bitonic sequence
        
        A bitonic sequence is a sequence that monotonically increases, then 
        monotonically decreases.
        
        Args:
            arr (list): Input list
            ascending (bool): Desired sorting direction
        """
        # Determine sequence length (power of 2)
        n = 1
        while n < len(arr):
            n *= 2
        
        # Pad with maximum values if needed
        while len(arr) < n:
            arr.append(float('inf') if ascending else float('-inf'))
        
        # Split list into half
        half_size = n // 2
        
        # Sort first half in ascending order
        for i in range(half_size):
            for j in range(i):
                if (ascending and arr[i] < arr[j]) or \
                   (not ascending and arr[i] > arr[j]):
                    arr[i], arr[j] = arr[j], arr[i]
        
        # Sort second half in descending order
        for i in range(half_size, n):
            for j in range(half_size, i):
                if (ascending and arr[i] > arr[j]) or \
                   (not ascending and arr[i] < arr[j]):
                    arr[i], arr[j] = arr[j], arr[i]
        
        return arr[:len(arr) - (n - len(arr))]
    
    # Convert to bitonic sequence and merge
    arr = convert_to_bitonic(arr, ascending)
    bitonic_merge(arr, 0, len(arr), ascending)
    
    return arr