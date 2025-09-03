"""
Write a python function to find the first non-repeated character in a given string.
assert first_non_repeating_character("abcabc") == None
"""
def first_non_repeating_character(s):
    # Create a dictionary to store the count of each character
    char_count = {}
    
    # Iterate over each character in the string
    for char in s:
        if char in char_count:
            # Increment the count if the character is already in the dictionary
            char_count[char] += 1
        else:
            # Set the count to 1 if the character is not in the dictionary
            char_count[char] = 1
    
    # Iterate over each character again to find the first non-repeating character
    for char in s:
        if char_count[char] == 1:
            return char
    
    # Return None if no non-repeating character is found
    return None

# Test the function with the provided test case
assert first_non_repeating_character("abcabc") == None
