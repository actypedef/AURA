"""
Write a function to count the number of characters in a string that occur at the same position in the string as in the English alphabet (case insensitive).
assert count_char_position("xbcefg") == 2
"""
def count_char_position(s):
    # Initialize the count to zero
    count = 0
    
    # Iterate over each character in the string
    for i in range(len(s)):
        # Check if the character's position matches its alphabetical position
        if s[i].lower() == chr(i + ord('a')):
            count += 1
    
    return count

# Test the function with the provided test case
assert count_char_position("xbcefg") == 2
