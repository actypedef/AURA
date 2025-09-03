"""
Write a python function to find the maximum difference between any two elements in a given array.
assert max_Abs_Diff((2,1,5,3)) == 4
"""
def max_Abs_Diff(arr):
    # Calculate the absolute difference between the maximum and minimum values in the array
    return abs(max(arr) - min(arr))

# Test the function with the provided test case
assert max_Abs_Diff((2, 1, 5, 3)) == 4
