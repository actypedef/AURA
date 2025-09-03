"""
Write a python function to find the first non-repeated character in a given string.
assert first_non_repeating_character("abcabc") == None
"""
def first_non_repeating_character(s):
    # Create a dictionary to store the frequency of each character
    char_count = {}
    
    # Iterate over each character in the string
    for char in s:
        if char in char_count:
            # Increment the count if the character is already in the dictionary
            char_count[char] += 1
        else:
            # Initialize the count to 1 if the character is not in the dictionary
            char_count[char] = 1
    
    # Iterate over each character in the string again
    for char in s:
        # Check if the count of the character is 1
        if char_count[char] == 1:
            # Return the first non-repeated character
            return char
    
    # If no non-repeated character is found, return None
    return None

# Test the function with the provided test case
assert first_non_repeating_character("abcabc") == None