"""
Write a python function to find the first repeated character in a given string.
assert first_repeated_char("abcabc") == "a"
"""
def first_repeated_char(str1):
    # Iterate through each character in the string
    for i in range(len(str1)):
        # Check if the character is repeated later in the string
        if str1[i] in str1[i + 1:]:
            return str1[i]
    # Return 'None' if no repeated character is found
    return None

# Test the function with the provided test case
assert first_repeated_char("abcabc") == "a"
