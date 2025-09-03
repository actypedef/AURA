"""
Write a function to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
assert change_date_format("2026-01-02") == '02-01-2026'
"""
import re

def change_date_format(dt):
    # Use regular expression to rearrange the date format from yyyy-mm-dd to dd-mm-yyyy
    return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', r'\3-\2-\1', dt)

# Test the function with the provided test case
assert change_date_format("2026-01-02") == '02-01-2026'
