"""
Write a function to reverse words seperated by spaces in a given string.
assert reverse_words("python program")==("program python")
"""
def reverse_words(s):
    # Split the string into words, reverse the list of words, and join them back with spaces
    return ' '.join(reversed(s.split()))

# Test the function with the provided test case
assert reverse_words("python program") == "program python"
