"""
Write a function to put spaces between words starting with capital letters in a given string.
assert capital_words_spaces("Python") == 'Python'
"""
def capital_words_spaces(text):
    # Iterate through each character in the text
    for i in range(len(text)):
        # Check if the current character is uppercase and it's not at the beginning of the string
        if text[i].isupper() and i != 0:
            # Insert a space before the uppercase letter
            text = text[:i] + " " + text[i:]
    return text

# Test the function with the provided test case
assert capital_words_spaces("Python") == 'Python'
