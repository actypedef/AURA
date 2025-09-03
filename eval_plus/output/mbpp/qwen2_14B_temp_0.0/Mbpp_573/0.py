"""
Write a python function to calculate the product of the unique numbers in a given list.
assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000
"""
def unique_product(nums):
    # Convert the list to a set to remove duplicates, then convert back to a list
    unique_nums = list(set(nums))
    
    # Initialize the product to 1 (multiplicative identity)
    product = 1
    
    # Calculate the product of the unique numbers
    for x in unique_nums:
        product *= x
    
    return product

# Test the function with the provided test case
assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) == 720000000
