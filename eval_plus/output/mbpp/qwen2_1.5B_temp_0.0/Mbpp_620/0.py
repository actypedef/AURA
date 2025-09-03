"""
Write a function to find the size of the largest subset of a list of numbers so that every pair is divisible.
assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4
"""
def largest_subset(nums):
    # Sort the array in ascending order
    nums.sort()
    
    # Initialize variables to keep track of the current subset size and the maximum subset size found
    current_size = 0
    max_size = 0
    
    # Iterate through the sorted array
    for i in range(len(nums)):
        # If the current number is divisible by the previous number in the subset,
        # add it to the subset
        if i > 0 and nums[i] % nums[i-1] == 0:
            current_size += 1
        else:
            # Otherwise, start a new subset from the current number
            current_size = 1
        
        # Update the maximum subset size found
        max_size = max(max_size, current_size)
    
    return max_size

# Test the function with the provided test case
assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4