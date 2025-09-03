"""
Write a function to count the number of characters in a string that occur at the same position in the string as in the English alphabet (case insensitive).
assert count_char_position("xbcefg") == 2
"""
def count_char_position(s):
    # Convert the string to lowercase to make the comparison case-insensitive
    s = s.lower()
    
    # Initialize a counter for matching characters
    match_count = 0
    
    # Iterate through each character in the string
    for i, char in enumerate(s):
        # Check if the character is a letter and its index matches its position in the alphabet
        if char.isalpha() and i + 1 == ord(char) - ord('a') + 1:
            match_count += 1
            
    return match_count

# Test cases to verify the correctness of the function
assert count_char_position("xbcefg") == 2
assert count_char_position("abcdefg") == 7
assert count_char_position("ABCDEFG") == 7
assert count_char_position("xyz") == 3
assert count_char_position("") == 0