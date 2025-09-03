"""
Write a python function that takes in a tuple and an element and counts the occcurences of the element in the tuple.
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),4) == 0
"""
def count_X(test_tup, X):
    # Count the occurrences of X in the tuple
    res = test_tup.count(X)
    return res

# Test the function with the provided test case
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 4) == 0
