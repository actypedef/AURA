"""
Write a python function to find the maximum difference between any two elements in a given array.
assert max_Abs_Diff((2,1,5,3)) == 4
"""
def max_Abs_Diff(arr):
    # Find the minimum and maximum values in the array
    min_val = min(arr)
    max_val = max(arr)
    
    # Calculate the absolute difference between the maximum and minimum values
    abs_diff = max_val - min_val
    
    return abs_diff

# Test the function with the provided test case
assert max_Abs_Diff((2,1,5,3)) == 4