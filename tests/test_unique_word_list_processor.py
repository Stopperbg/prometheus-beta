import os
import pytest
from src.unique_word_list_processor import process_word_list

def test_basic_word_list_processing(tmp_path):
    # Create a temporary file with test words
    test_file = tmp_path / "word_list.txt"
    test_file.write_text("apple\nbanana\ncherry\napple\nDATE\ndate\n")
    
    # Process the file
    result = process_word_list(str(test_file))
    
    # Check the result
    assert result == ['apple', 'banana', 'cherry', 'date']

def test_empty_file(tmp_path):
    # Create an empty file
    test_file = tmp_path / "empty_list.txt"
    test_file.write_text("")
    
    # Process the file
    result = process_word_list(str(test_file))
    
    # Check the result
    assert result == []

def test_file_with_only_whitespace(tmp_path):
    # Create a file with only whitespace
    test_file = tmp_path / "whitespace_list.txt"
    test_file.write_text("  \n \t \n   ")
    
    # Process the file
    result = process_word_list(str(test_file))
    
    # Check the result
    assert result == []

def test_file_not_found():
    # Check that FileNotFoundError is raised for non-existent file
    with pytest.raises(FileNotFoundError, match="The file non_existent_file.txt was not found."):
        process_word_list("non_existent_file.txt")

def test_complex_sorting_and_deduplication(tmp_path):
    # Create a file with complex sorting scenario
    test_file = tmp_path / "complex_list.txt"
    test_file.write_text("Zebra\naardvark\nLion\nlion\naardvark\n")
    
    # Process the file
    result = process_word_list(str(test_file))
    
    # Check the result
    assert result == ['aardvark', 'lion', 'zebra']