"""
Write a python function takes in an integer and check whether the frequency of each digit in the integer is less than or equal to the digit itself.
assert validate(1234) == True
"""
def validate(n):
    # Convert the number to a string to iterate over each digit
    s = str(n)
    
    # Iterate over each unique digit in the string representation of the number
    for i in set(s):
        # Count the frequency of the current digit in the string
        if s.count(i) > int(i):
            return False
    
    return True

# Test the function with the provided test case
assert validate(1234) == True
