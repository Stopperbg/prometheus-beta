import pytest
from src.unique_grid_paths import get_unique_coordinate_combinations

def test_basic_coordinate_combinations():
    """Test basic functionality with simple coordinate pairs."""
    coordinates = [(1, 2), (3, 4), (1, 4), (3, 2)]
    expected = [(1, 2), (1, 4), (3, 2), (3, 4)]
    assert get_unique_coordinate_combinations(coordinates) == expected

def test_duplicate_coordinates():
    """Test handling of duplicate coordinates."""
    coordinates = [(1, 1), (1, 1), (2, 2), (2, 2)]
    expected = [(1, 1), (1, 2), (2, 1), (2, 2)]
    assert get_unique_coordinate_combinations(coordinates) == expected

def test_empty_list():
    """Test behavior with an empty list of coordinates."""
    coordinates = []
    expected = []
    assert get_unique_coordinate_combinations(coordinates) == expected

def test_single_coordinate():
    """Test with a single coordinate pair."""
    coordinates = [(5, 7)]
    expected = [(5, 7)]
    assert get_unique_coordinate_combinations(coordinates) == expected

def test_invalid_input_type():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list of coordinate pairs"):
        get_unique_coordinate_combinations("not a list")

def test_invalid_coordinate_type():
    """Test raising ValueError for invalid coordinate pairs."""
    with pytest.raises(ValueError, match="Each coordinate must be a tuple of two elements"):
        get_unique_coordinate_combinations([(1, 2), "invalid"])

def test_negative_coordinates():
    """Test handling of negative coordinate values."""
    coordinates = [(-1, 2), (0, -3), (1, 0)]
    expected = [(-1, -3), (-1, 0), (-1, 2), (0, -3), (0, 0), (0, 2), (1, -3), (1, 0), (1, 2)]
    assert get_unique_coordinate_combinations(coordinates) == expected