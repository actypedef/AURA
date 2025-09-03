"""
Write a function to check if the given tuples contain the k or not.
assert check_K((10, 4, 5, 6, 8), 6) == True
"""
def check_K(tuples, k):
    # Check if the tuple contains the element k
    return k in tuples

# Test cases
assert check_K((10, 4, 5, 6, 8), 6) == True
assert check_K((1, 2, 3, 4, 5), 7) == False
assert check_K(('a', 'b', 'c'), 'd') == False
assert check_K((True, False, True), True) == True
assert check_K((None, None, None), None) == True