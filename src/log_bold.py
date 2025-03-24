def log_bold(message):
    """
    Log a message in bold text to the console.

    Args:
        message (str): The message to be logged in bold.

    Returns:
        str: The bold-formatted message.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(message, str):
        raise TypeError("Input must be a string")
    
    # ANSI escape codes for bold text
    BOLD_START = "\033[1m"
    BOLD_END = "\033[0m"
    
    # Return the bolded message
    return f"{BOLD_START}{message}{BOLD_END}"