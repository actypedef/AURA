"""
Write a function to find all words which are at least 4 characters long in a string.
assert set(find_char_long('Please move back to stream')) == set(['Please', 'move', 'back', 'stream'])
"""
def find_char_long(text):
    """
    Write a function to find all words which are at least 4 characters long in a string.
    """
    # Split the input text into words
    words = text.split()
    
    # Filter words that are at least 4 characters long
    long_words = [word for word in words if len(word) >= 4]
    
    return long_words

# Test cases
assert set(find_char_long('Please move back to stream')) == set(['Please', 'move', 'back', 'stream'])
assert set(find_char_long('The quick brown fox jumps over the lazy dog')) == set(['quick', 'brown', 'jumps', 'over', 'lazy'])
assert set(find_char_long('A')) == set([])
assert set(find_char_long('')) == set([])
assert set(find_char_long('This is a test')) == set(['This', 'test'])
assert set(find_char_long('This is a test with some long words')) == set(['This', 'test', 'with', 'some', 'long', 'words'])