"""
Write a function to check if a string represents an integer or not.
assert check_integer("python")==False
"""
def check_integer(s):
    # Check if the string is empty or consists only of whitespace characters
    if len(s.strip()) == 0:
        return False
    
    # Iterate through each character in the string
    for i in range(len(s)):
        # If the character is not a digit and not a sign at the beginning, it's not an integer
        if (i != 0 and s[i] not in '0123456789') or (s[0] in '+-' and i > 0):
            return False
    
    # If all checks pass, the string is an integer
    return True

# Test the function with the provided test case
assert check_integer("python") == False