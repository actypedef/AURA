"""
Write a python function to find the sum of the product of consecutive binomial co-efficients.
assert sum_Of_product(3) == 15
"""
def sum_Of_product(n):
    # Initialize the result variable to store the sum of products
    res = 0
    
    # Iterate through each number from 2 to n (inclusive)
    for i in range(2, n + 1):
        # Calculate the product of binomial coefficients C(i, j) * C(i, j-1)
        res += (i * (i - 1))
    
    return res

# Test the function with the provided test case
assert sum_Of_product(3) == 15