"""
Write a function to check if given tuple contains no duplicates.
assert check_distinct((1, 4, 5, 6, 1, 4)) == False
"""
def check_distinct(test_tup):
    # Convert the tuple into a set to remove duplicates
    res = len(set(test_tup)) == len(test_tup)
    return res

# Test the function with the provided test case
assert check_distinct((1, 4, 5, 6, 1, 4)) == False
