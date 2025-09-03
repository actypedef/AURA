"""
Write a function to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
assert change_date_format("2026-01-02") == '02-01-2026'
"""
def change_date_format(date_str):
    # Split the input string into year, month, and day components
    year, month, day = map(int, date_str.split('-'))
    
    # Format the date as dd-mm-yyyy
    formatted_date = f"{day}-{month}-{year}"
    
    return formatted_date

# Test cases to verify the correctness of the function
assert change_date_format("2026-01-02") == '02-01-2026'
assert change_date_format("2023-10-15") == '15-10-2023'
assert change_date_format("2020-04-30") == '30-04-2020'