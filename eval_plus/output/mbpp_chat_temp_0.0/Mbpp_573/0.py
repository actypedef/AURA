"""
Write a python function to calculate the product of the unique numbers in a given list.
assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000
"""
def unique_product(nums):
    # Initialize the product variable to 1 (since multiplying by 1 has no effect)
    product = 1
    
    # Iterate through each number in the list
    for num in nums:
        # Multiply the current product by the number if it's not already in the set
        if num not in set(nums):
            product *= num
    
    # Return the final product
    return product

# Test the function with the provided test case
assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) == 720000000