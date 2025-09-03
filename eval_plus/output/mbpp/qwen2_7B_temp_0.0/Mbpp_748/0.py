"""
Write a function to put spaces between words starting with capital letters in a given string.
assert capital_words_spaces("Python") == 'Python'
"""
def capital_words_spaces(text):
    # Initialize an empty list to store the words
    words = []
    
    # Iterate over each character in the text
    for char in text:
        # Check if the character is uppercase
        if char.isupper():
            # If it's not the first word, add a space before adding the new word
            if len(words) > 0:
                words.append(' ')
            words.append(char)
        else:
            # Add lowercase characters directly
            words.append(char)
    
    # Join all elements in the list into a single string
    return ''.join(words)

# Test the function with the provided test case
assert capital_words_spaces("Python") == 'Python'
