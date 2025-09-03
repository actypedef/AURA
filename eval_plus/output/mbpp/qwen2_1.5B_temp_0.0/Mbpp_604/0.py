"""
Write a function to reverse words seperated by spaces in a given string.
assert reverse_words("python program")==("program python")
"""
def reverse_words(s):
    # Split the string into words using space as the delimiter
    words = s.split()
    # Reverse the list of words
    reversed_words = words[::-1]
    # Join the reversed list of words back into a single string
    return ' '.join(reversed_words)

# Test cases to verify the correctness of the solution
assert reverse_words("python program") == "program python"
assert reverse_words("hello world") == "world hello"
assert reverse_words("") == ""
assert reverse_words("single word") == "single word"