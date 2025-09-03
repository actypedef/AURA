"""
Write a python function to remove the characters which have odd index values of a given string.
assert odd_values_string('abcdef') == 'ace'
"""
def odd_values_string(s):
    # Initialize an empty string to store the result
    result = ''
    # Iterate over the string using enumerate to get both index and character
    for i, char in enumerate(s):
        # Check if the index is even (0-based indexing)
        if i % 2 == 0:
            # Append the character to the result string
            result += char
    return result

# Test cases to verify the correctness of the solution
assert odd_values_string('abcdef') == 'ace'
assert odd_values_string('hello world') == 'el ol'
assert odd_values_string('123456789') == '2468'
assert odd_values_string('a') == 'a'