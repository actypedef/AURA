"""
Write a function to multiply all the numbers in a list and divide with the length of the list.
assert math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001)
"""
import math

def multiply_num(test_tup):
    # Initialize result to 1 (since multiplying by 1 has no effect)
    res = 1
    
    # Iterate through each element in the tuple
    for ele in test_tup:
        # Multiply the current result by the element
        res *= ele
    
    # Divide the result by the length of the tuple
    res /= len(test_tup)
    
    return res

# Test the function with the provided test case
assert math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001)