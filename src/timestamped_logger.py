import logging
import os
import sys

def log_with_timestamp(message, log_level='INFO', log_file=None):
    """
    Log a message with a timestamp to both console and file.
    
    Args:
        message (str): The message to be logged
        log_level (str, optional): Logging level. Defaults to 'INFO'.
                                   Supports 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'
        log_file (str, optional): Path to the log file. If None, uses system-dependent temp file.
    
    Raises:
        ValueError: If an invalid log level is provided
    
    Returns:
        bool: True if logging was successful
    """
    # Determine log file path
    if log_file is None:
        log_file = os.path.join(os.getcwd(), 'default.log')
    
    # Ensure the directory exists
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
    
    # Flush logs to ensure writing
    logging.shutdown()
    
    return True  # Indicates successful logging