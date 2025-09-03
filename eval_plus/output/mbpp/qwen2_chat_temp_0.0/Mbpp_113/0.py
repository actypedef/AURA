"""
Write a function to check if a string represents an integer or not.
assert check_integer("python")==False
"""
def check_integer(s):
    # Check if the string is empty
    if s == "":
        return False
    
    # Initialize a flag for negative numbers
    flag = 0
    
    # If the first character is '-', set flag to 1 and remove the '-' sign
    if s[0] == '-':
        flag = 1
        s = s[1:]
    
    # Iterate through each character in the string
    for i in range(len(s)):
        # Check if the current character is not a digit
        if s[i] < '0' or s[i] > '9':
            return False
    
    # Return True if no non-digit characters were found
    return True

# Test the function with the provided test case
assert check_integer("python") == False
