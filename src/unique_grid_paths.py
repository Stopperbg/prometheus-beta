def get_unique_coordinate_combinations(coordinates):
    """
    Generate a list of unique x and y coordinate combinations in ascending order.
    
    Args:
        coordinates (list): A list of coordinate pairs [(x1, y1), (x2, y2), ...]
    
    Returns:
        list: A sorted list of unique (x, y) combinations
    
    Raises:
        TypeError: If input is not a list of coordinate pairs
        ValueError: If any coordinate pair is not a tuple of two elements
    """
    # Validate input
    if not isinstance(coordinates, list):
        raise TypeError("Input must be a list of coordinate pairs")
    
    # Validate each coordinate pair
    for coord in coordinates:
        if not isinstance(coord, tuple) or len(coord) != 2:
            raise ValueError("Each coordinate must be a tuple of two elements")
    
    # Extract unique x and y values
    unique_x = sorted(set(coord[0] for coord in coordinates))
    unique_y = sorted(set(coord[1] for coord in coordinates))
    
    # Generate all unique combinations
    unique_combinations = []
    for x in unique_x:
        for y in unique_y:
            unique_combinations.append((x, y))
    
    return sorted(unique_combinations)