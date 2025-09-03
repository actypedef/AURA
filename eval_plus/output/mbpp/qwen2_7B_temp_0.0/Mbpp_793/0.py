"""
Write a python function to find the last position of an element in a sorted array.
assert last([1,2,3],1) == 0
"""
def last(arr, x):
    # Initialize the result variable to -1, indicating that the element has not been found yet
    res = -1
    
    # Iterate through each index and value in the array using enumerate
    for i, val in enumerate(arr):
        # If the current value matches the target value x, update the result to the current index
        if val == x:
            res = i
    
    # Return the final result, which will be the last index where the element was found or -1 if it was not found
    return res

# Test the function with the provided test case
assert last([1, 2, 3], 1) == 0
