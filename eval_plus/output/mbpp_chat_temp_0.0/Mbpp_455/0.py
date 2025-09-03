"""
Write a function to check whether the given month number contains 31 days or not.
assert check_monthnumb_number(5)==True
"""
def check_monthnumb_number(month):
    # Check if the month number is one of those that typically have 31 days
    return month in [1, 3, 5, 7, 8, 10, 12]

# Test the function with the provided test case
assert check_monthnumb_number(5) == True
