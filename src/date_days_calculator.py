from datetime import datetime, date

def calculate_days_between_dates(start_date, end_date):
    """
    Calculate the number of days between two dates.

    Args:
        start_date (str or datetime or date): The start date
        end_date (str or datetime or date): The end date

    Returns:
        int: The number of days between the two dates (absolute value)

    Raises:
        ValueError: If the input dates are invalid or cannot be parsed
    """
    # Convert inputs to date objects if they are strings
    if isinstance(start_date, str):
        try:
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        except ValueError:
            raise ValueError("Invalid start date format. Use YYYY-MM-DD")

    if isinstance(end_date, str):
        try:
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        except ValueError:
            raise ValueError("Invalid end date format. Use YYYY-MM-DD")

    # Convert datetime to date if necessary
    if isinstance(start_date, datetime):
        start_date = start_date.date()
    if isinstance(end_date, datetime):
        end_date = end_date.date()

    # Validate date type
    if not (isinstance(start_date, date) and isinstance(end_date, date)):
        raise ValueError("Inputs must be date, datetime, or valid date strings")

    # Calculate and return absolute number of days
    return abs((end_date - start_date).days)