"""
Write a function to check whether the given month number contains 31 days or not.
assert check_monthnumb_number(5)==True
"""
def check_monthnumb_number(month_num):
    # Check if the month number is between 1 and 12 (inclusive)
    if 1 <= month_num <= 12:
        # If it's February, return True because February has 28 or 29 days
        if month_num == 2:
            return True
        else:
            # For other months, return False because they do not have 31 days
            return False
    else:
        # If the month number is not between 1 and 12, return False
        return False

# Test cases to verify the correctness of the function
assert check_monthnumb_number(5) == True
assert check_monthnumb_number(4) == False
assert check_monthnumb_number(12) == True
assert check_monthnumb_number(1) == False
assert check_monthnumb_number(13) == False