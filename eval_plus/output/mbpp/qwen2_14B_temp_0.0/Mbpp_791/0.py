"""
Write a function to remove tuples from the given tuple.
assert remove_nested((1, 5, 7, (4, 6), 10)) == (1, 5, 7, 10)
"""
def flatten(test_tuple):
    # Create an empty list to store non-tuple elements
    res = []
    
    # Iterate through each element in the tuple
    for count in test_tuple:
        # Check if the element is not a tuple
        if not isinstance(count, tuple):
            # If not a tuple, append it to the result list
            res.append(count)
    
    # Convert the list back to a tuple and return it
    return tuple(res)

# Test the function with the provided test case
assert flatten((1, 5, 7, (4, 6), 10)) == (1, 5, 7, 10)