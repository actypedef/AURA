"""
Write a function to find the maximum product subarray of the given array.
assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
"""
def max_subarray_product(nums):
    if not nums:
        return 0
    
    max_product = min_product = result = nums[0]
    
    for num in nums[1:]:
        if num < 0:
            max_product, min_product = min_product, max_product
        
        max_product = max(num, max_product * num)
        min_product = min(num, min_product * num)
        
        result = max(result, max_product)
    
    return result

# Test cases
assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
assert max_subarray_product([-2, 0, -1]) == 0
assert max_subarray_product([]) == 0
assert max_subarray_product([-1, -2, -3, -4]) == 24