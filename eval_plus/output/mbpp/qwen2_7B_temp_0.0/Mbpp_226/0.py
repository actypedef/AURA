"""
Write a python function to remove the characters which have odd index values of a given string.
assert odd_values_string('abcdef') == 'ace'
"""
def odd_values_string(str1):
    # Initialize an empty string to store the result
    result = ""
    # Iterate over the string using enumerate to get both index and character
    for index, char in enumerate(str1):
        # Check if the index is even (since index starts at 0)
        if index % 2 == 0:
            # Append the character to the result string
            result += char
    return result

# Test the function with the provided test case
assert odd_values_string('abcdef') == 'ace'
