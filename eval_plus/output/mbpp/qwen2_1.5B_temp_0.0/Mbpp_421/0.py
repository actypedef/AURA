"""
Write a function to concatenate each element of tuple by the delimiter.
assert concatenate_tuple(("ID", "is", 4, "UTS") ) == 'ID-is-4-UTS'
"""
def concatenate_tuple(tup):
    # Initialize an empty string to store the concatenated result
    result = ""
    # Iterate over each element in the tuple
    for item in tup:
        # Convert the item to a string and append it to the result with the delimiter
        result += str(item) + "-"
    # Return the final concatenated string without the trailing delimiter
    return result[:-1]

# Test the function with the provided test case
assert concatenate_tuple(("ID", "is", 4, "UTS")) == 'ID-is-4-UTS'