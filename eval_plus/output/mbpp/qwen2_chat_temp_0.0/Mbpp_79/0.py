"""
Write a python function to check whether the length of the word is odd or not.
assert word_len("Hadoop") == False
"""
def word_len(word):
    # Check if the length of the word is even
    return len(word) % 2 == 0

# Test the function with the provided test case
assert word_len("Hadoop") == False
