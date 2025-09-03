"""
Write a function to perform index wise multiplication of tuple elements in the given two tuples.
assert index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3)) ) == ((6, 21), (12, 45), (2, 9), (7, 30))
"""
def index_multiplication(test_tup1, test_tup2):
    # Initialize an empty list to store the result
    res = []
    # Iterate over the range of the length of the first tuple
    for idx in range(len(test_tup1)):
        # Multiply the elements at the current index from both tuples and append to the result list
        res.append(tuple(map(lambda x, y: x * y, test_tup1[idx], test_tup2[idx])))
    return tuple(res)

# Test the function with the provided test case
assert index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))) == ((6, 21), (12, 45), (2, 9), (7, 30))