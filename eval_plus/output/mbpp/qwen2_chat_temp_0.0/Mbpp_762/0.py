"""
Write a function to check whether the given month number contains 30 days or not. Months are given as number from 1 to 12.
assert check_monthnumber_number(6)==True
"""
def check_monthnumber_number(month):
    # Check if the month has exactly 30 days
    return month == 4 or month == 6 or month == 9 or month == 11

# Test the function with the provided test case
assert check_monthnumber_number(6) == True