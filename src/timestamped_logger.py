import logging
from datetime import datetime
import os

def log_with_timestamp(message, log_level='INFO', log_file='app.log'):
    """
    Log a message with a timestamp to both console and file.
    
    Args:
        message (str): The message to be logged
        log_level (str, optional): Logging level. Defaults to 'INFO'.
                                   Supports 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'
        log_file (str, optional): Path to the log file. Defaults to 'app.log'.
    
    Raises:
        ValueError: If an invalid log level is provided
        IOError: If there are issues creating or writing to the log file
    """
    # Ensure the logs directory exists
    os.makedirs(os.path.dirname(log_file) or '.', exist_ok=True)
    
    # Configure logging
    logging.basicConfig(
        level=logging.getLevelName(log_level.upper()),
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename=log_file,
        filemode='a'
    )
    
    # Get the appropriate logging method based on log level
    log_method = {
        'DEBUG': logging.debug,
        'INFO': logging.info,
        'WARNING': logging.warning,
        'ERROR': logging.error,
        'CRITICAL': logging.critical
    }.get(log_level.upper())
    
    # Validate log level
    if not log_method:
        raise ValueError(f"Invalid log level: {log_level}. Must be one of: DEBUG, INFO, WARNING, ERROR, CRITICAL")
    
    # Log the message
    log_method(message)
    
    return True  # Indicates successful logging