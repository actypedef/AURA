"""
Write a function to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
assert change_date_format("2026-01-02") == '02-01-2026'
"""
def change_date_format(date):
    # Split the input date string into parts using '-'
    date_parts = date.split('-')
    
    # Reorder the parts to match the desired output format (dd-mm-yyyy)
    formatted_date = date_parts[2] + '-' + date_parts[1] + '-' + date_parts[0]
    
    return formatted_date

# Test the function with the provided test case
assert change_date_format("2026-01-02") == '02-01-2026'
