"""
Write a python function to find a pair with highest product from a given array of integers.
assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)
"""
def max_Product(nums):
    # Initialize the maximum product and the pair with the smallest product
    max_product = nums[0] * nums[1]
    max_pair = (nums[0], nums[1])
    
    # Iterate through each pair of numbers in the list
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            # Calculate the product of the current pair
            product = nums[i] * nums[j]
            
            # Update the maximum product and the corresponding pair if the current product is larger
            if product > max_product:
                max_product = product
                max_pair = (nums[i], nums[j])
    
    return max_pair

# Test the function with the provided test case
assert max_Product([1, 2, 3, 4, 7, 0, 8, 4]) == (7, 8)
