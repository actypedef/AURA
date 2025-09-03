"""
Write a python function takes in an integer and check whether the frequency of each digit in the integer is less than or equal to the digit itself.
assert validate(1234) == True
"""
def validate(n):
    # Convert the number to a string to iterate over its digits
    s = str(n)
    
    # Iterate through each unique digit in the string representation of n
    for i in set(s):
        # Count the occurrences of the current digit in the string
        count = s.count(i)
        
        # Check if the count of the digit is greater than the digit itself
        if count > int(i):
            return False
    
    # If all conditions are met, return True
    return True

# Test the function with the provided test case
assert validate(1234) == True
