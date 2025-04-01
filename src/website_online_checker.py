import requests
from typing import Union, Tuple

def is_website_online(url: str, timeout: int = 5) -> Tuple[bool, str]:
    """
    Check if a website is online and reachable.

    Args:
        url (str): The URL of the website to check
        timeout (int, optional): Connection timeout in seconds. Defaults to 5.

    Returns:
        Tuple[bool, str]: A tuple containing:
            - Boolean indicating if the website is online
            - Descriptive message about the connection status
    """
    # Validate URL input
    if not url or not isinstance(url, str):
        return False, "Invalid URL provided"

    # Ensure URL starts with http:// or https://
    if not url.startswith(('http://', 'https://')):
        url = f'https://{url}'

    try:
        # Send a GET request with a timeout
        response = requests.get(url, timeout=timeout)
        
        # Check if request was successful
        if response.status_code == 200:
            return True, f"Website {url} is online (Status Code: 200)"
        else:
            return False, f"Website returned status code: {response.status_code}"

    except requests.exceptions.ConnectionError:
        return False, f"Connection error: Unable to reach {url}"
    except requests.exceptions.Timeout:
        return False, f"Connection timed out after {timeout} seconds"
    except requests.exceptions.RequestException as e:
        return False, f"Error checking website: {str(e)}"