"""
Write a function to that returns true if the input string contains sequences of lowercase letters joined with an underscore and false otherwise.
assert text_lowercase_underscore("aab_cbbbc")==(True)
"""
def text_lowercase_underscore(text):
    # Check if the text contains only lowercase letters joined with an underscore
    return text.islower() and '_' in text

# Test cases to verify the correctness of the function
assert text_lowercase_underscore("aab_cbbbc") == (True)
assert text_lowercase_underscore("aab_Cbbbc") == (False)
assert text_lowercase_underscore("123abc") == (False)
assert text_lowercase_underscore("a_b_c") == (True)
assert text_lowercase_underscore("A_b_c") == (False)