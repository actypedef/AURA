"""
Write a python function to find the first non-repeated character in a given string.
assert first_non_repeating_character("abcabc") == None
"""
def first_non_repeating_character(s):
    # Create a dictionary to store the count of each character
    char_count = {}
    
    # Count the occurrences of each character in the string
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Iterate through the string again to find the first non-repeated character
    for char in s:
        if char_count[char] == 1:
            return char
    
    # If no non-repeated character is found, return None
    return None

# Test cases to verify the correctness of the function
assert first_non_repeating_character("abcabc") == None
assert first_non_repeating_character("aabbcc") == "d"
assert first_non_repeating_character("abcdefg") == "a"
assert first_non_repeating_character("aabbcdd") == "c"
assert first_non_repeating_character("") == None