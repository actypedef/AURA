"""
Write a function to find the cumulative sum of all the values that are present in the given tuple list.
assert cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30
"""
def cummulative_sum(test_list):
    # Initialize the sum to zero
    summ = 0
    
    # Iterate through each tuple in the list
    for sub in test_list:
        # Sum up all elements in the current tuple and add to the total sum
        summ += sum(sub)
    
    return summ

# Test the function with the provided test case
assert cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30
