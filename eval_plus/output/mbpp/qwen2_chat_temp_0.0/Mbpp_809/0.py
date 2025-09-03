"""
Write a function to check if each element of second tuple is smaller than its corresponding element in the first tuple.
assert check_smaller((1, 2, 3), (2, 3, 4)) == False
"""
def check_smaller(test_tup1, test_tup2):
    # Check if all elements in test_tup2 are less than their corresponding elements in test_tup1
    res = all(x < y for x, y in zip(test_tup1, test_tup2))
    return res

# Test the function with the provided test case
assert check_smaller((1, 2, 3), (2, 3, 4)) == False
