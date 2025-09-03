"""
Write a python function to find the first non-repeated character in a given string.
assert first_non_repeating_character("abcabc") == None
"""
def first_non_repeating_character(s):
    # Dictionary to store the count of each character
    char_count = {}
    
    # Count the occurrences of each character in the string
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Find the first character with a count of 1
    for char in s:
        if char_count[char] == 1:
            return char
    
    # Return None if no non-repeating character is found
    return None

# Test the function with the provided test case
assert first_non_repeating_character("abcabc") == None
