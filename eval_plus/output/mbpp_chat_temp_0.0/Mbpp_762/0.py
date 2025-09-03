"""
Write a function to check whether the given month number contains 30 days or not. Months are given as number from 1 to 12.
assert check_monthnumber_number(6)==True
"""
def check_monthnumber_number(n):
    # Check if the month number is one of those with 30 days
    return n == 4 or n == 6 or n == 9 or n == 11

# Test the function with the provided test case
assert check_monthnumber_number(6) == True
