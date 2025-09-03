"""
Write a function to find the cumulative sum of all the values that are present in the given tuple list.
assert cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30
"""
def cummulative_sum(test_list):
    # Initialize the result variable to store the cumulative sum
    res = 0
    
    # Iterate through each sublist in the test list
    for sub in test_list:
        # Add each element in the sublist to the result
        res += sum(sub)
    
    # Return the final cumulative sum
    return res

# Test the function with the provided test case
assert cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30
