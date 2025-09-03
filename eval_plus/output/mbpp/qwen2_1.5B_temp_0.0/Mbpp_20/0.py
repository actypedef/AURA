"""
Write a function to check if the given number is woodball or not.
assert is_woodall(383) == True
"""
def is_woodall(n):
    # Check if n is less than 100
    if n < 100:
        return False
    
    # Calculate the sum of digits
    sum_of_digits = sum(int(digit) for digit in str(n))
    
    # Check if the sum of digits is equal to n
    return sum_of_digits == n

# Test cases
assert is_woodall(383) == True