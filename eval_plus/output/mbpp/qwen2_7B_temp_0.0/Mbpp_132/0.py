"""
Write a function to convert a tuple to a string.
assert tup_string(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's'))==("exercises")
"""
def tup_string(tup):
    # Joining tuple elements into a single string
    result = ''.join(tup)
    return result

# Test case to verify the function works as expected
assert tup_string(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')) == "exercises"
