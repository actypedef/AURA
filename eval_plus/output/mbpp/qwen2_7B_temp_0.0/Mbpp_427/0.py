"""
Write a function to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
assert change_date_format("2026-01-02") == '02-01-2026'
"""
def change_date_format(date):
    # Split the input date string into year, month, and day components
    year, month, day = date.split('-')
    
    # Reformat the date to dd-mm-yyyy format
    reformatted_date = f"{day}-{month}-{year}"
    
    return reformatted_date

# Test the function with the provided test case
assert change_date_format("2026-01-02") == '02-01-2026'
