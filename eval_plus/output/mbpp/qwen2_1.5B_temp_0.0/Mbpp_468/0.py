"""
Write a function to find the maximum product formed by multiplying numbers of an increasing subsequence of that array.
assert max_product([3, 100, 4, 5, 150, 6]) == 3000
"""
def max_product(nums):
    # Initialize variables to keep track of the maximum product found so far and the current product
    max_product = nums[0]
    current_product = nums[0]
    
    # Iterate through the list starting from the second element
    for num in nums[1:]:
        # If the current number is greater than the current product, update the current product
        if num > current_product:
            current_product = num
        else:
            # Otherwise, reset the current product to the current number
            current_product = num
        
        # Update the maximum product if the current product is greater
        if current_product > max_product:
            max_product = current_product
    
    return max_product

# Test cases to verify the correctness of the solution
assert max_product([3, 100, 4, 5, 150, 6]) == 3000
assert max_product([1, -2, -3, 0, 7, 8, 9]) == 5040
assert max_product([-1, -2, -3, -4]) == 24
assert max_product([10, 20, 30, 40, 50]) == 120000