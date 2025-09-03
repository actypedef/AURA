"""
Write a function to remove tuples from the given tuple.
assert remove_nested((1, 5, 7, (4, 6), 10)) == (1, 5, 7, 10)
"""
def remove_nested(tup):
    # Initialize an empty list to store non-tuple elements
    result = []
    
    # Iterate through each element in the input tuple
    for item in tup:
        # Check if the current item is not a tuple
        if not isinstance(item, tuple):
            # If it's not a tuple, append it to the result list
            result.append(item)
    
    # Convert the result list back into a tuple and return it
    return tuple(result)

# Test the function with the provided test case
assert remove_nested((1, 5, 7, (4, 6), 10)) == (1, 5, 7, 10)