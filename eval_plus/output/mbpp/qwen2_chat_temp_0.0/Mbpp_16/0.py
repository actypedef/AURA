"""
Write a function to that returns true if the input string contains sequences of lowercase letters joined with an underscore and false otherwise.
assert text_lowercase_underscore("aab_cbbbc")==(True)
"""
def text_lowercase_underscore(text):
    # Check if the entire string consists of lowercase letters separated by underscores
    return text == '_'.join(x for x in text.split('_') if x.islower())

# Test the function with the provided test case
assert text_lowercase_underscore("aab_cbbbc") == True