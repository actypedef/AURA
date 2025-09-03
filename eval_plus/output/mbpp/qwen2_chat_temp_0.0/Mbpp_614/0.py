"""
Write a function to find the cumulative sum of all the values that are present in the given tuple list.
assert cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30
"""
def cummulative_sum(test_list):
    # Initialize the result variable to zero
    res = 0
    
    # Iterate through each sublist in the test list
    for sub in test_list:
        # Add up all elements in the current sublist and add to the result
        res += sum(sub)
    
    # Return the total cumulative sum
    return res

# Test the function with the provided test case
assert cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30
