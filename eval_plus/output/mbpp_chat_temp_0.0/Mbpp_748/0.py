"""
Write a function to put spaces between words starting with capital letters in a given string.
assert capital_words_spaces("Python") == 'Python'
"""
def capital_words_spaces(text):
    # Split the text into words based on capital letters
    words = re.findall('[A-Z][^A-Z]*', text)
    
    # Join the words with spaces
    return ' '.join(words)

# Test the function with the provided test case
assert capital_words_spaces("Python") == 'Python'