"""
Write a function to find all words which are at least 4 characters long in a string.
assert set(find_char_long('Please move back to stream')) == set(['Please', 'move', 'back', 'stream'])
"""
def find_char_long(text):
    # Split the text into words using space as a delimiter
    words = text.split(" ")
    
    # Filter out words that have less than 4 characters
    result = [word for word in words if len(word) >= 4]
    
    return result

# Test the function with the provided test case
assert set(find_char_long('Please move back to stream')) == set(['Please', 'move', 'back', 'stream'])
