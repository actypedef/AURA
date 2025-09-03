"""
Write a function to reverse words seperated by spaces in a given string.
assert reverse_words("python program")==("program python")
"""
def reverse_words(s):
    # Split the input string into words using space as a delimiter
    words = s.split(' ')
    
    # Reverse the list of words
    reversed_words = words[::-1]
    
    # Join the reversed list of words back into a single string with spaces
    result = ' '.join(reversed_words)
    
    return result

# Test the function with the provided test case
assert reverse_words("python program") == "program python"
