def remove_duplicate_words(input_string):
    """
    Remove duplicate words from a given string while preserving the original order.
    
    Args:
        input_string (str): The input string containing words to be deduplicated.
    
    Returns:
        str: A new string with duplicate words removed, maintaining the first occurrence order.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> remove_duplicate_words("hello world hello python world")
        'hello world python'
        >>> remove_duplicate_words("a b c a b c")
        'a b c'
        >>> remove_duplicate_words("")
        ''
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not input_string:
        return ""
    
    # Split the string into words
    words = input_string.split()
    
    # Use a set to track seen words while preserving order
    seen_words = set()
    unique_words = []
    
    for word in words:
        if word not in seen_words:
            unique_words.append(word)
            seen_words.add(word)
    
    # Join the unique words back into a string
    return " ".join(unique_words)