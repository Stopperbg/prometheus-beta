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
        log_file (str, optional): Path to the log file. If None, uses system temp directory.
    
    Raises:
        ValueError: If an invalid log level is provided
    
    Returns:
        bool: True if logging was successful
    """
    # Determine log file path
    if log_file is None:
        log_file = os.path.join(tempfile.gettempdir(), 'default.log')
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(log_file) or '.', exist_ok=True)
    
    # Create a logger
    logger = logging.getLogger(log_file)
    logger.setLevel(logging.getLevelName(log_level.upper()))
    
    # Create file handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    ))
    
    # Add the file handler to the logger
    logger.addHandler(file_handler)
    
    # Get the appropriate logging method based on log level
    log_method = {
        'DEBUG': logger.debug,
        'INFO': logger.info,
        'WARNING': logger.warning,
        'ERROR': logger.error,
        'CRITICAL': logger.critical
    }.get(log_level.upper())
    
    # Validate log level
    if not log_method:
        raise ValueError(f"Invalid log level: {log_level}. Must be one of: DEBUG, INFO, WARNING, ERROR, CRITICAL")
    
    # Log the message
    log_method(message)
    
    # Ensure log is written and remove handler
    file_handler.flush()
    logger.removeHandler(file_handler)
    file_handler.close()
    
    return True  # Indicates successful logging