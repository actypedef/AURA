"""
Write a function to check whether the given month number contains 30 days or not. Months are given as number from 1 to 12.
assert check_monthnumber_number(6)==True
"""
def check_monthnumber_number(month):
    # Check if the month number is between 4 and 7 (inclusive)
    if 4 <= month <= 7:
        return True
    else:
        return False

# Test the function with the provided test case
assert check_monthnumber_number(6) == True
