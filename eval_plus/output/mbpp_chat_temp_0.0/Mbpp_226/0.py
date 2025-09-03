"""
Write a python function to remove the characters which have odd index values of a given string.
assert odd_values_string('abcdef') == 'ace'
"""
def odd_values_string(str1):
    # Initialize an empty string to store the result
    result = ""
    
    # Iterate over the string using enumerate to get both index and character
    for i, char in enumerate(str1):
        # Check if the index is even (since we want characters at odd positions)
        if i % 2 == 0:
            # Append the character to the result string
            result += char
    
    # Return the resulting string
    return result

# Test the function with the provided test case
assert odd_values_string('abcdef') == 'ace'
