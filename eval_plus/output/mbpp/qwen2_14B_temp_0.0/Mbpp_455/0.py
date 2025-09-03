"""
Write a function to check whether the given month number contains 31 days or not.
assert check_monthnumb_number(5)==True
"""
def check_monthnumb_number(monthnumb):
    # List of months with 31 days
    months_with_31_days = [1, 3, 5, 7, 8, 10, 12]
    
    # Check if the given month number is in the list
    return monthnumb in months_with_31_days

# Test the function with the provided test case
assert check_monthnumb_number(5) == True
