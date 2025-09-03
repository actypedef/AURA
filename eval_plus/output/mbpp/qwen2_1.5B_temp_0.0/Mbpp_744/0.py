"""
Write a function to check if the given tuple has any none value or not.
assert check_none((10, 4, 5, 6, None)) == True
"""
def check_none(tup):
    # Check if any element in the tuple is None
    return any(element is None for element in tup)

# Test cases to verify the correctness of the function
assert check_none((10, 4, 5, 6, None)) == True
assert check_none((10, 4, 5, 6)) == False
assert check_none(('a', 'b', 'c')) == False
assert check_none((None, None, None)) == True