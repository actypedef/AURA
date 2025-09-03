"""
Write a function to check whether the given month number contains 31 days or not.
assert check_monthnumb_number(5)==True
"""
def check_monthnumb_number(n):
    # Check if the month number is between 1 and 12
    if n < 1 or n > 12:
        return False
    
    # List of months with 31 days
    months_with_31_days = [1, 3, 5, 7, 8, 10, 12]
    
    # Return True if the month number is in the list, otherwise False
    return n in months_with_31_days

# Test the function with the provided test case
assert check_monthnumb_number(5) == True
