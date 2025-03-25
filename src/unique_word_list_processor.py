def process_word_list(input_file_path):
    """
    Read a text file containing words, remove duplicates, and return a sorted unique list.

    Args:
        input_file_path (str): Path to the text file containing words.

    Returns:
        list: A sorted list of unique words.

    Raises:
        FileNotFoundError: If the input file cannot be found.
        IOError: If there is an error reading the file.
    """
    try:
        # Read words from the file, strip whitespace, and convert to lowercase
        with open(input_file_path, 'r') as file:
            # Read lines, strip whitespace, and filter out empty lines
            words = [word.strip().lower() for word in file.readlines() if word.strip()]
        
        # Remove duplicates and sort
        unique_sorted_words = sorted(set(words))
        
        return unique_sorted_words
    
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {input_file_path} was not found.")
    except IOError as e:
        raise IOError(f"Error reading the file {input_file_path}: {str(e)}")