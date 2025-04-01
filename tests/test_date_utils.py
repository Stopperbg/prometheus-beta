import pytest
from datetime import datetime, timedelta
from src.date_utils import add_days_to_date

def test_add_days_to_datetime():
    """Test adding days to a datetime object."""
    base_date = datetime(2023, 1, 1)
    result = add_days_to_date(base_date, 5)
    assert result == datetime(2023, 1, 6)

def test_add_days_to_date_string():
    """Test adding days to a date string."""
    result = add_days_to_date('2023-01-01', 5)
    assert result == datetime(2023, 1, 6)

def test_subtract_days():
    """Test subtracting days (negative input)."""
    base_date = datetime(2023, 1, 10)
    result = add_days_to_date(base_date, -5)
    assert result == datetime(2023, 1, 5)

def test_invalid_date_type():
    """Test invalid date type raises TypeError."""
    with pytest.raises(TypeError):
        add_days_to_date(123, 5)

def test_invalid_days_type():
    """Test invalid days type raises ValueError."""
    with pytest.raises(ValueError):
        add_days_to_date(datetime(2023, 1, 1), '5')

def test_invalid_date_string():
    """Test invalid date string format raises ValueError."""
    with pytest.raises(ValueError):
        add_days_to_date('2023/01/01', 5)

def test_leap_year():
    """Test adding days across leap year boundary."""
    base_date = datetime(2024, 2, 28)
    result = add_days_to_date(base_date, 1)
    assert result == datetime(2024, 2, 29)

def test_large_day_addition():
    """Test adding a large number of days."""
    base_date = datetime(2023, 1, 1)
    result = add_days_to_date(base_date, 365)
    assert result == datetime(2024, 1, 1)

def test_zero_days():
    """Test adding zero days returns the same date."""
    base_date = datetime(2023, 1, 1)
    result = add_days_to_date(base_date, 0)
    assert result == base_date