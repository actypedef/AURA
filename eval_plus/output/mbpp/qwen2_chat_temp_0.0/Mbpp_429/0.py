"""
Write a function to extract the elementwise and tuples from the given two tuples.
assert and_tuples((10, 4, 6, 9), (5, 2, 3, 3)) == (0, 0, 2, 1)
"""
def and_tuples(test_tup1, test_tup2):
    # Initialize an empty list to store results
    res = []
    
    # Iterate over pairs of elements from both tuples using zip
    for ele1, ele2 in zip(test_tup1, test_tup2):
        # Calculate the AND operation on each pair and append to the result list
        res.append(ele1 & ele2)
    
    # Convert the result list back to a tuple and return it
    return tuple(res)

# Test the function with the provided test case
assert and_tuples((10, 4, 6, 9), (5, 2, 3, 3)) == (0, 0, 2, 1)
