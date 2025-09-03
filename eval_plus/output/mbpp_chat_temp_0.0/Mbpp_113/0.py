"""
Write a function to check if a string represents an integer or not.
assert check_integer("python")==False
"""
def check_integer(s):
    # Check if the string is empty
    if len(s) == 0:
        return False
    
    # Check for leading '+' or '-' signs
    i = 1 if s[0] in "+-" else 0
    
    # Iterate through the characters of the string
    while i < len(s):
        # If the character is not a digit, return False
        if not s[i].isdigit():
            return False
        i += 1
    
    # If all characters are digits, return True
    return True

# Test the function with the provided test case
assert check_integer("python") == False
