"""
Write a python function to find the first digit of a given number.
assert first_Digit(123) == 1
"""
def first_Digit(n):
    # Convert the number to a string to easily access the first character
    s = str(n)
    
    # Return the first character as an integer
    return int(s[0])

# Test the function with the provided test case
assert first_Digit(123) == 1
