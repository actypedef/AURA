"""
Write a function to check whether the product of numbers in a list is even or not.
assert is_product_even([1,2,3])
"""
def is_product_even(lst):
    # Iterate through each number in the list
    for num in lst:
        # Check if the number is even
        if num % 2 == 0:
            return True
    # If no even number is found, return False
    return False

# Test the function with the provided test case
assert is_product_even([1, 2, 3]) == True
