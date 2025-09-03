"""
Write a function to convert a tuple to a string.
assert tup_string(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's'))==("exercises")
"""
def tup_string(tup):
    # Joining tuple elements into a string using join() method
    result = ''.join(tup)
    return result

# Test the function with the provided test case
assert tup_string(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')) == "exercises"
