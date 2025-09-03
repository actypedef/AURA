"""
Write a function to find the sum of numbers in a list within a range specified by two indices.
assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10) == 29
"""
def sum_range_list(list_nums, start_index, end_index):
    # Initialize the sum variable to zero
    total_sum = 0
    
    # Iterate over the range from start_index to end_index (inclusive)
    for i in range(start_index, end_index + 1):
        # Add each number in the specified range to the total_sum
        total_sum += list_nums[i]
    
    # Return the computed sum
    return total_sum

# Test the function with the provided test case
assert sum_range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], 8, 10) == 29
