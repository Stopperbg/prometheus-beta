def bubble_sort(arr):
    """
    Implement the bubble sort algorithm to sort a list in ascending order.
    
    Args:
        arr (list): The input list to be sorted.
    
    Returns:
        list: A new sorted list in ascending order.
    
    Raises:
        TypeError: If the input is not a list.
        TypeError: If the list contains elements that cannot be compared.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a copy of the input list to avoid modifying the original
    sorted_arr = arr.copy()
    
    # Outer loop for passes
    for i in range(len(sorted_arr)):
        # Flag to optimize the algorithm by breaking early if no swaps occur
        swapped = False
        
        # Inner loop for comparing and swapping adjacent elements
        for j in range(0, len(sorted_arr) - i - 1):
            # Compare adjacent elements
            try:
                if sorted_arr[j] > sorted_arr[j + 1]:
                    # Swap elements
                    sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                    swapped = True
            except TypeError:
                raise TypeError("List contains elements that cannot be compared")
        
        # If no swapping occurred, list is already sorted
        if not swapped:
            break
    
    return sorted_arr