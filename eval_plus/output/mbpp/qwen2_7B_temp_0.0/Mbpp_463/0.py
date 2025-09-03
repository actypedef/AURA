"""
Write a function to find the maximum product subarray of the given array.
assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
"""
def max_subarray_product(arr):
    # Initialize variables to store the maximum product so far and the current product
    max_product = float('-inf')
    curr_product = 1
    
    # Iterate through each element in the array
    for i in range(len(arr)):
        # Update the current product by multiplying it with the current element
        curr_product *= arr[i]
        
        # If the current product is greater than the maximum product, update the maximum product
        if curr_product > max_product:
            max_product = curr_product
        
        # Reset the current product to 1 if it becomes zero or negative
        if curr_product <= 0:
            curr_product = 1
    
    return max_product

# Test the function with the provided test case
assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112