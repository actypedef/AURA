"""
Write a python function to check whether the length of the word is odd or not.
assert word_len("Hadoop") == False
"""
def word_len(word):
    return len(word) % 2 != 0

# Test cases
assert word_len("Hadoop") == False
assert word_len("Python") == True
assert word_len("Java") == False
assert word_len("JavaScript") == True