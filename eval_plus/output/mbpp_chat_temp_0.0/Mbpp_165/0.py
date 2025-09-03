"""
Write a function to count the number of characters in a string that occur at the same position in the string as in the English alphabet (case insensitive).
assert count_char_position("xbcefg") == 2
"""
def count_char_position(s):
    # Initialize a counter for matching positions
    match = 0
    
    # Iterate over each character in the string using enumerate to get both index and character
    for i, c in enumerate(s):
        # Check if the character's position matches its alphabetical order (case insensitive)
        if ord(c.lower()) - ord('a') == i:
            match += 1
    
    # Return the total count of matching positions
    return match

# Test the function with the provided test case
assert count_char_position("xbcefg") == 2
