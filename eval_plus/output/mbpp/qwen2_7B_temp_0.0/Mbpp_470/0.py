"""
Write a function to find the pairwise addition of the neighboring elements of the given tuple.
assert add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)
"""
def add_pairwise(test_tup):
    # Initialize an empty list to store the results
    res = []
    # Iterate through the tuple using enumerate to get both index and value
    for idx in range(len(test_tup) - 1):
        # Add the current element and the next element together
        res.append(test_tup[idx] + test_tup[idx + 1])
    return tuple(res)

# Test the function with the provided test case
assert add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)