"""
Write a python function to check whether all the characters are same or not.
assert all_Characters_Same("python") == False
"""
def all_Characters_Same(str):
    # Check if the string has only one character or is empty
    if len(str) <= 1:
        return True
    
    # Get the first character of the string
    first_char = str[0]
    
    # Iterate through each character in the string
    for char in str:
        # If any character is different from the first character, return False
        if char != first_char:
            return False
    
    # If all characters are the same, return True
    return True

# Test the function with the provided test case
assert all_Characters_Same("python") == False
