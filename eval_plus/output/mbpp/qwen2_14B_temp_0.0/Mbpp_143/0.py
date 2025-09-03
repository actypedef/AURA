"""
Write a function to find number of lists present in the given tuple.
assert find_lists(([1, 2, 3, 4], [5, 6, 7, 8])) == 2
"""
def find_lists(input_tuple):
    # Initialize a counter for list elements
    result = 0
    
    # Iterate through each element in the tuple
    for element in input_tuple:
        # Check if the element is of type list
        if isinstance(element, list):
            result += 1  # Increment the counter if it is a list
    
    return result

# Test the function with the provided test case
assert find_lists(([1, 2, 3, 4], [5, 6, 7, 8])) == 2
