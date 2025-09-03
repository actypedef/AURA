"""
Write a function to find the ascii value of a character.
assert ascii_value('A')==65
"""
def ascii_value(char):
    # Use the ord() function to get the ASCII value of the character
    return ord(char)

# Test the function with the provided test case
assert ascii_value('A') == 65
