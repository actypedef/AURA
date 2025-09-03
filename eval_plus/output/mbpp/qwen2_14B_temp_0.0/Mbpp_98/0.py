"""
Write a function to multiply all the numbers in a list and divide with the length of the list.
assert math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001)
"""
import math

def multiply_num(numbers):
    # Initialize the product to 1 (multiplicative identity)
    product = 1
    
    # Iterate through each number in the list and multiply it to the product
    for x in numbers:
        product *= x
    
    # Divide the product by the length of the list
    return product / len(numbers)

# Test the function with the provided test case
assert math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001)
