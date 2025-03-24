from colorama import Fore, Back, Style, init
import sys

# Initialize colorama for cross-platform color support
init(autoreset=True)

def log_with_color(message, 
                   text_color=None, 
                   background_color=None, 
                   level='info', 
                   file=sys.stdout):
    """
    Log a message with optional text and background colors.

    Args:
        message (str): The message to log
        text_color (str, optional): Color of the text. 
            Supports: 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white', 'black'
        background_color (str, optional): Background color of the text.
            Supports: 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white', 'black'
        level (str, optional): Log level. Defaults to 'info'. 
            Can be 'info', 'warning', 'error', 'debug'
        file (file, optional): File-like object to write to. Defaults to sys.stdout

    Raises:
        ValueError: If an invalid color or log level is provided
    """
    # Color mapping
    color_map = {
        'red': Fore.RED,
        'green': Fore.GREEN,
        'yellow': Fore.YELLOW,
        'blue': Fore.BLUE,
        'magenta': Fore.MAGENTA,
        'cyan': Fore.CYAN,
        'white': Fore.WHITE,
        'black': Fore.BLACK
    }

    background_map = {
        'red': Back.RED,
        'green': Back.GREEN,
        'yellow': Back.YELLOW,
        'blue': Back.BLUE,
        'magenta': Back.MAGENTA,
        'cyan': Back.CYAN,
        'white': Back.WHITE,
        'black': Back.BLACK
    }

    # Validate log level
    valid_levels = ['info', 'warning', 'error', 'debug']
    if level not in valid_levels:
        raise ValueError(f"Invalid log level. Must be one of {valid_levels}")

    # Validate colors
    if text_color and text_color.lower() not in color_map:
        raise ValueError(f"Invalid text color. Must be one of {list(color_map.keys())}")
    
    if background_color and background_color.lower() not in background_map:
        raise ValueError(f"Invalid background color. Must be one of {list(background_map.keys())}")

    # Construct color formatting
    text_color_code = color_map.get(text_color.lower(), '') if text_color else ''
    background_color_code = background_map.get(background_color.lower(), '') if background_color else ''

    # Prefix for log levels
    level_prefixes = {
        'info': '[INFO] ',
        'warning': '[WARNING] ',
        'error': '[ERROR] ',
        'debug': '[DEBUG] '
    }

    # Construct the formatted message
    formatted_message = f"{text_color_code}{background_color_code}{level_prefixes[level]}{message}{Style.RESET_ALL}"

    # Write to the specified file
    print(formatted_message, file=file, flush=True)