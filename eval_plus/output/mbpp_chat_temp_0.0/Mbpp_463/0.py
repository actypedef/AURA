"""
Write a function to find the maximum product subarray of the given array.
assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
"""
def max_subarray_product(arr):
    # Initialize variables to store the maximum product so far,
    # the maximum product ending at the current position, and
    # the minimum product ending at the current position.
    max_so_far = arr[0]
    max_ending_here = arr[0]
    min_ending_here = arr[0]
    
    # Iterate through the array starting from the second element.
    for i in range(1, len(arr)):
        # If the current element is negative, swap the maximum and minimum products.
        if arr[i] < 0:
            max_ending_here, min_ending_here = min_ending_here, max_ending_here
        
        # Update the maximum product ending at the current position.
        max_ending_here = max(max_ending_here * arr[i], arr[i])
        
        # Update the minimum product ending at the current position.
        min_ending_here = min(min_ending_here * arr[i], arr[i])
        
        # Update the maximum product found so far.
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far

# Test the function with the provided test case
assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112