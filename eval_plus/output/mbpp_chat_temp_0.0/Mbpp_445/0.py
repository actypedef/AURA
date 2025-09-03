"""
Write a function to perform index wise multiplication of tuple elements in the given two tuples.
assert index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3)) ) == ((6, 21), (12, 45), (2, 9), (7, 30))
"""
def index_multiplication(test_tup1, test_tup2):
    # Using list comprehension for element-wise multiplication
    res = tuple(tuple(x * y for x, y in zip(inner_tup1, inner_tup2))
                for inner_tup1, inner_tup2 in zip(test_tup1, test_tup2))
    return res

# Test the function with the provided test case
assert index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))) == ((6, 21), (12, 45), (2, 9), (7, 30))