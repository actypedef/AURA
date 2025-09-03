"""
Write a function to find all words which are at least 4 characters long in a string.
assert set(find_char_long('Please move back to stream')) == set(['Please', 'move', 'back', 'stream'])
"""
def find_char_long(s):
    # Split the input string into words using space as delimiter
    words = s.split()
    # Filter out words that are at least 4 characters long
    result = [word for word in words if len(word) >= 4]
    return set(result)

# Test the function
assert set(find_char_long('Please move back to stream')) == set(['Please', 'move', 'back', 'stream'])