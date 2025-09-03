"""
Write a function to find the cumulative sum of all the values that are present in the given tuple list.
assert cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30
"""
def cummulative_sum(tup_list):
    # Initialize the total sum to zero
    total_sum = 0
    
    # Iterate over each tuple in the list
    for tup in tup_list:
        # Add the sum of the current tuple to the total sum
        total_sum += sum(tup)
    
    # Return the final cumulative sum
    return total_sum

# Test cases to verify the correctness of the function
assert cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30
assert cummulative_sum([(10, 20), (30, 40, 50), (60, 70)]) == 280
assert cummulative_sum([(0, 0, 0), (1, 1, 1), (2, 2, 2)]) == 9