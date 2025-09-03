
def valid_date(date):
    """You have to write a function which validates a given date string and
    returns True if the date is valid otherwise False.
    The date is valid if all of the following rules are satisfied:
    1. The date string is not empty.
    2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
    3. The months should not be less than 1 or higher than 12.
    4. The date should be in the format: mm-dd-yyyy

    for example: 
    valid_date('03-11-2000') => True

    valid_date('15-01-2012') => False

    valid_date('04-0-2040') => False

    valid_date('06-04-2020') => True

    valid_date('06/04/2020') => False
    """
import re

def valid_date(date):
    # Check if the date string is not empty
    if not date:
        return False
    
    # Define the regex pattern for the date format mm-dd-yyyy
    date_pattern = r'^\d{1,2}-\d{1,2}-\d{4}$'
    
    # Check if the date matches the pattern
    if not re.match(date_pattern, date):
        return False
    
    # Split the date into month, day, and year
    month, day, year = map(int, date.split('-'))
    
    # Check if the month is within the valid range (1-12)
    if month < 1 or month > 12:
        return False
    
    # Check if the day is within the valid range based on the month
    if month == 2:
        if day < 1 or day > 29:
            return False
    elif month in [4, 6, 9, 11]:
        if day < 1 or day > 30:
            return False
    else:
        if day < 1 or day > 31:
            return False
    
    # If all checks pass, the date is valid
    return True

# Test cases