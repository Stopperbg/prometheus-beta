import pytest
from datetime import datetime, date, timedelta
from src.date_days_calculator import calculate_days_between_dates

def test_calculate_days_between_dates_same_date():
    """Test calculating days between the same date returns 0"""
    assert calculate_days_between_dates('2023-01-01', '2023-01-01') == 0
    assert calculate_days_between_dates(date(2023, 1, 1), date(2023, 1, 1)) == 0

def test_calculate_days_between_dates_different_dates():
    """Test calculating days between different dates"""
    assert calculate_days_between_dates('2023-01-01', '2023-01-10') == 9
    assert calculate_days_between_dates('2023-01-10', '2023-01-01') == 9

def test_calculate_days_between_dates_datetime_input():
    """Test input with datetime objects"""
    start = datetime(2023, 1, 1)
    end = datetime(2023, 1, 10)
    assert calculate_days_between_dates(start, end) == 9

def test_calculate_days_between_dates_date_objects():
    """Test input with date objects"""
    start = date(2023, 1, 1)
    end = date(2023, 1, 10)
    assert calculate_days_between_dates(start, end) == 9

def test_calculate_days_between_dates_across_years():
    """Test calculating days between dates across different years"""
    assert calculate_days_between_dates('2022-12-31', '2023-01-01') == 1

def test_calculate_days_between_dates_invalid_input():
    """Test handling of invalid date inputs"""
    with pytest.raises(ValueError, match="Invalid start date format"):
        calculate_days_between_dates('invalid-date', '2023-01-01')
    
    with pytest.raises(ValueError, match="Invalid end date format"):
        calculate_days_between_dates('2023-01-01', 'invalid-date')

def test_calculate_days_between_dates_invalid_type():
    """Test handling of invalid input types"""
    with pytest.raises(ValueError, match="Inputs must be date"):
        calculate_days_between_dates(123, '2023-01-01')
    
    with pytest.raises(ValueError, match="Inputs must be date"):
        calculate_days_between_dates('2023-01-01', [1, 2, 3])