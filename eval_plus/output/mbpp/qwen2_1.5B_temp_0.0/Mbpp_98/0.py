"""
Write a function to multiply all the numbers in a list and divide with the length of the list.
assert math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001)
"""
import math

def multiply_num(lst):
    # Calculate the product of all elements in the list
    product = 1
    for num in lst:
        product *= num
    
    # Divide the product by the length of the list
    result = product / len(lst)
    
    return result

# Test the function with the provided test case
assert math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001)