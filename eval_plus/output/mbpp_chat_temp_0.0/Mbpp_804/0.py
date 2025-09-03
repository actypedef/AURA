"""
Write a function to check whether the product of numbers in a list is even or not.
assert is_product_even([1,2,3])
"""
def is_product_even(numbers):
    # Initialize the product variable to 1 (since multiplying by 1 has no effect)
    product = 1
    
    # Iterate through each number in the list
    for num in numbers:
        # Multiply the current product by the number
        product *= num
    
    # Check if the final product is even
    return product % 2 == 0

# Test the function with the provided test case
assert is_product_even([1, 2, 3]) == False