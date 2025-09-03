"""
Write a function to multiply all the numbers in a list and divide with the length of the list.
assert math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001)
"""
import math

def multiply_num(nums):
    # Initialize the product variable to 1 (since multiplying by 1 has no effect)
    product = 1
    
    # Loop through each number in the tuple and multiply it to the product
    for num in nums:
        product *= num
    
    # Divide the product by the length of the tuple to get the average product
    return product / len(nums)

# Test the function with the provided test case
assert math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001)