"""
Write a python function to find the maximum difference between any two elements in a given array.
assert max_Abs_Diff((2,1,5,3)) == 4
"""
def max_Abs_Diff(arr):
    # Initialize minimum and maximum element as first element of array
    min_element = arr[0]
    max_element = arr[0]
    
    # Iterate through the array to find the minimum and maximum elements
    for i in range(1, len(arr)):
        if arr[i] < min_element:
            min_element = arr[i]
        elif arr[i] > max_element:
            max_element = arr[i]
    
    # Return the absolute difference between the maximum and minimum elements
    return abs(max_element - min_element)

# Test the function with the provided test case
assert max_Abs_Diff((2, 1, 5, 3)) == 4