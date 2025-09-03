"""
Write a python function to find the last position of an element in a sorted array.
assert last([1,2,3],1) == 0
"""
def last(arr, x):
    # Initialize the result variable to -1
    res = -1
    
    # Iterate through each index and value in the array
    for i, val in enumerate(arr):
        # Check if the current value matches the target value
        if (val == x):
            # Update the result to the current index
            res = i
    
    # Return the last found index or -1 if not found
    return res

# Test the function with the provided test case
assert last([1, 2, 3], 1) == 0