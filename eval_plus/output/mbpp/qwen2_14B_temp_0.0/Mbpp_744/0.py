"""
Write a function to check if the given tuple has any none value or not.
assert check_none((10, 4, 5, 6, None)) == True
"""
def check_none(test_tup):
    # Check if None is present in the tuple
    res = None in test_tup
    return (res) 

# Test the function with the provided test case
assert check_none((10, 4, 5, 6, None)) == True
