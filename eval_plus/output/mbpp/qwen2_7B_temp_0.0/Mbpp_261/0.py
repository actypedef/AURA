"""
Write a function that takes in two tuples and performs mathematical division operation element-wise across the given tuples.
assert division_elements((10, 4, 6, 9),(5, 2, 3, 3)) == (2, 2, 2, 3)
"""
def division_elements(test_tup1, test_tup2):
    # Using map() to perform division of elements from both tuples
    res = tuple(map(lambda x, y: x / y, test_tup1, test_tup2))
    return res

# Test the function with the provided data point
assert division_elements((10, 4, 6, 9), (5, 2, 3, 3)) == (2, 2, 2, 3)
