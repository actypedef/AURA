"""
Write a function to find the number of elements that occurs before the tuple element in the given tuple.
assert count_first_elements((1, 5, 7, (4, 6), 10) ) == 3
"""
def count_first_elements(input_tuple):
    # Initialize a counter for the first elements
    count = 0
    
    # Iterate through each element in the input tuple
    for element in input_tuple:
        # Check if the current element is not a tuple
        if not isinstance(element, tuple):
            # Increment the counter
            count += 1
    
    # Return the final count
    return count

# Test the function with the provided data point
assert count_first_elements((1, 5, 7, (4, 6), 10)) == 3