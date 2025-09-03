"""
Write a python function to calculate the product of the unique numbers in a given list.
assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000
"""
def unique_product(nums):
    # Use set to remove duplicates and then calculate the product of the remaining elements
    return reduce(lambda x, y: x * y, set(nums))

# Test the function with the provided test case
assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) == 720000000
