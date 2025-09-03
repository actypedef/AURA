"""
Write a function to check whether the given month number contains 31 days or not.
assert check_monthnumb_number(5)==True
"""
def check_monthnumb_number(month):
    # Check if the month has 31 days
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return True
    else:
        return False

# Test the function with the provided test case
assert check_monthnumb_number(5) == True
