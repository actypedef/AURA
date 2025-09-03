"""
Write a function to find the number of elements that occurs before the tuple element in the given tuple.
assert count_first_elements((1, 5, 7, (4, 6), 10) ) == 3
"""
def count_first_elements(test_tup):
    # Initialize counter for elements before the tuple
    res = 0
    
    # Iterate through each element in the tuple
    for ele in test_tup:
        # Check if the current element is a tuple
        if isinstance(ele, tuple):
            break
        # Increment counter for non-tuple elements
        res += 1
    
    return res

# Test the function with the provided test case
assert count_first_elements((1, 5, 7, (4, 6), 10)) == 3
