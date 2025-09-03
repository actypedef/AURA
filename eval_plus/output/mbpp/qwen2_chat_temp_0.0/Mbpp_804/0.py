"""
Write a function to check whether the product of numbers in a list is even or not.
assert is_product_even([1,2,3])
"""
def is_product_even(numbers):
    # Check if all numbers in the list are even
    return all(x % 2 == 0 for x in numbers)

# Test the function with the provided test case
assert is_product_even([1, 2, 3]) == False
