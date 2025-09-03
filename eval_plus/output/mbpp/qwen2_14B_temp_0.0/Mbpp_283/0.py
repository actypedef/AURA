"""
Write a python function takes in an integer and check whether the frequency of each digit in the integer is less than or equal to the digit itself.
assert validate(1234) == True
"""
def validate(n):
    # Convert the integer to a string to iterate over each digit
    for i in str(n):
        # Check if the frequency of the digit is greater than the digit itself
        if str(n).count(i) > int(i):
            return False
    return True

# Test the function with the provided test case
assert validate(1234) == True
