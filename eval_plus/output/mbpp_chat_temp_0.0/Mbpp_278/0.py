"""
Write a function to find the number of elements that occurs before the tuple element in the given tuple.
assert count_first_elements((1, 5, 7, (4, 6), 10) ) == 3
"""
def count_first_elements(test_tup):
    # Initialize counter to zero
    res = 0
    # Iterate through each element in the tuple
    for ele in test_tup:
        # Check if the current element is not a tuple
        if not isinstance(ele, tuple):
            # Increment the counter if it's not a tuple
            res += 1
        else:
            # Break the loop once a tuple is encountered
            break
    return res

# Test the function with the provided test case
assert count_first_elements((1, 5, 7, (4, 6), 10)) == 3