"""
Write a function to maximize the given two tuples.
assert maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))) == ((6, 7), (4, 9), (2, 9), (7, 10))
"""
def maximize_elements(test_tup1, test_tup2):
    # Use zip to pair elements from both tuples and max to select the maximum value from each pair
    res = tuple(max(ele1, ele2) for ele1, ele2 in zip(test_tup1, test_tup2))
    return res

# Test the function with the provided test case
assert maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))) == ((6, 7), (4, 9), (2, 9), (7, 10))
