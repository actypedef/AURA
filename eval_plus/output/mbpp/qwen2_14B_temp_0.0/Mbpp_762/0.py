"""
Write a function to check whether the given month number contains 30 days or not. Months are given as number from 1 to 12.
assert check_monthnumber_number(6)==True
"""
def check_monthnumber_number(monthnumber1):
    # Check if the month number is one of the months with 30 days
    if monthnumber1 in (4, 6, 9, 11):
        return True
    else:
        return False

# Test the function with the provided test case
assert check_monthnumber_number(6) == True
