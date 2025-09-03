"""
Write a python function to find the maximum difference between any two elements in a given array.
assert max_Abs_Diff((2,1,5,3)) == 4
"""
def max_Abs_Diff(arr):
    # Initialize the minimum and maximum values in the array
    min_val = arr[0]
    max_val = arr[0]
    
    # Iterate through the array to find the minimum and maximum values
    for i in range(1, len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
        elif arr[i] > max_val:
            max_val = arr[i]
    
    # Calculate the absolute difference between the maximum and minimum values
    diff = abs(max_val - min_val)
    
    return diff

# Test the function with the provided test case
assert max_Abs_Diff((2, 1, 5, 3)) == 4
