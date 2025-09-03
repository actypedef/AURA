"""
Write a function to find the maximum product subarray of the given array.
assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
"""
def max_subarray_product(nums):
    # Initialize the maximum product, minimum product, and result to the first element of the array
    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]
    
    # Iterate through the array starting from the second element
    for num in nums[1:]:
        # If the current number is negative, swap max_product and min_product
        if num < 0:
            max_product, min_product = min_product, max_product
        
        # Update max_product and min_product
        max_product = max(num, max_product * num)
        min_product = min(num, min_product * num)
        
        # Update the result with the maximum value found so far
        result = max(result, max_product)
    
    return result

# Test the function with the provided test case
assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
