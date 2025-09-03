"""
Write a python function to remove the characters which have odd index values of a given string.
assert odd_values_string('abcdef') == 'ace'
"""
def odd_values_string(str):
    # Initialize an empty string to store characters at even indices
    result = ""
    
    # Iterate through the string using index
    for i in range(len(str)):
        # Check if the index is even
        if i % 2 == 0:
            # Append the character at the even index to the result
            result += str[i]
    
    return result

# Test the function with the provided test case
assert odd_values_string('abcdef') == 'ace'
