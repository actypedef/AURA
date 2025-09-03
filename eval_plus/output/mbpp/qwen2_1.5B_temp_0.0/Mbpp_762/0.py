"""
Write a function to check whether the given month number contains 30 days or not. Months are given as number from 1 to 12.
assert check_monthnumber_number(6)==True
"""
def check_monthnumber_number(month):
    # Check if the month number is between 1 and 12 (inclusive)
    if month >= 1 and month <= 12:
        # If it's February, return True because February has 28 or 29 days
        if month == 2:
            return True
        # For other months, return False because they have either 30 or 31 days
        else:
            return False
    else:
        # If the month number is out of range, return None
        return None

# Test cases to verify the correctness of the function
assert check_monthnumber_number(6) == True
assert check_monthnumber_number(4) == False
assert check_monthnumber_number(12) == True
assert check_monthnumber_number(13) == None