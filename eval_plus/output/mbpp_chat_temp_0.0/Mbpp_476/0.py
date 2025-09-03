"""
Write a python function to find the sum of the largest and smallest value in a given array.
assert big_sum([1,2,3]) == 4
"""
def big_sum(arr):
    # Calculate the sum of the maximum and minimum values in the array
    return max(arr) + min(arr)

# Test the function with the provided test case
assert big_sum([1, 2, 3]) == 4
