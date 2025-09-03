"""
Write a python function takes in an integer and check whether the frequency of each digit in the integer is less than or equal to the digit itself.
assert validate(1234) == True
"""
def validate(n):
    # Convert the number to a string to iterate over each digit
    for i in str(n):
        # Count the occurrences of the current digit in the number
        if n.count(int(i)) > int(i):
            return False
    return True

# Test the function with the provided test case
assert validate(1234) == True
