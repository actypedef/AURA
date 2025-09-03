"""
Write a python function to find the sum of the largest and smallest value in a given array.
assert big_sum([1,2,3]) == 4
"""
def big_sum(arr):
    # Find the maximum and minimum values in the array
    max_val = max(arr)
    min_val = min(arr)
    
    # Return the sum of the maximum and minimum values
    return max_val + min_val

# Test the function with the provided test case
assert big_sum([1, 2, 3]) == 4