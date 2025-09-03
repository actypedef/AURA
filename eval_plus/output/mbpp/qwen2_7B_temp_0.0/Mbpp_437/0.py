"""
Write a function to remove odd characters in a string.
assert remove_odd("python")==("yhn")
"""
def remove_odd(s):
    # Initialize an empty string to store even-indexed characters
    result = ""
    
    # Iterate over the string using enumerate to get both index and character
    for i, char in enumerate(s):
        # Check if the index is even (i.e., character position is even)
        if i % 2 == 0:
            # Append the character to the result string
            result += char
    
    # Return the resulting string without odd characters
    return result

# Test the function with the provided test case
assert remove_odd("python") == "yhn"
