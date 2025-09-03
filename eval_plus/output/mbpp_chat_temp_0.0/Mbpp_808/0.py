"""
Write a function to check if the given tuples contain the k or not.
assert check_K((10, 4, 5, 6, 8), 6) == True
"""
def check_K(test_tup, K):
    # Check if 'K' is present in the tuple 'test_tup'
    res = K in test_tup
    return res

# Test the function with the provided test case
assert check_K((10, 4, 5, 6, 8), 6) == True
