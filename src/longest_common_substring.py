def find_longest_common_substring(str1: str, str2: str) -> str:
    """
    Find the longest common substring between two input strings.
    
    Args:
        str1 (str): The first input string
        str2 (str): The second input string
    
    Returns:
        str: The longest common substring. If no common substring exists, 
             returns an empty string.
    
    Time Complexity: O(m*n), where m and n are lengths of input strings
    Space Complexity: O(m*n)
    
    Examples:
        >>> find_longest_common_substring("hello", "help")
        'hel'
        >>> find_longest_common_substring("programming", "program")
        'program'
        >>> find_longest_common_substring("abc", "xyz")
        ''
    """
    # Handle edge cases
    if not str1 or not str2:
        return ""
    
    # Create a matrix to store lengths of common substrings
    m, n = len(str1), len(str2)
    # Initialize the dynamic programming matrix
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Variables to track the longest substring
    max_length = 0
    candidate_substrings = []
    
    # Fill the dynamic programming matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Case-sensitive matching
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                
                # Track maximum length substrings
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    candidate_substrings = [str1[i-max_length:i]]
                elif dp[i][j] == max_length:
                    candidate_substrings.append(str1[i-max_length:i])
    
    # Return the first candidate substring if found
    return candidate_substrings[0] if candidate_substrings else ""