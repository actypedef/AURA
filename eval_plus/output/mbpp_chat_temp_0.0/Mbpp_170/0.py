"""
Write a function to find the sum of numbers in a list within a range specified by two indices.
assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10) == 29
"""
def sum_range_list(nums, l, r):
    # Initialize the sum variable to store the result
    total_sum = 0
    
    # Iterate through the sublist from index l to r (inclusive)
    for i in range(l, r + 1):
        # Add each element in the sublist to the total sum
        total_sum += nums[i]
    
    # Return the computed sum
    return total_sum

# Test the function with the provided test case
assert sum_range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], 8, 10) == 29