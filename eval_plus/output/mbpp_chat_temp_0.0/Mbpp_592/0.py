"""
Write a python function to find the sum of the product of consecutive binomial co-efficients.
assert sum_Of_product(3) == 15
"""
def sum_Of_product(n):
    # Initialize the result variable to store the sum of products
    res = 0
    
    # Iterate through each value of k from 1 to n-1
    for k in range(1, n):
        # Calculate the product of binomial coefficients C(n, k) * C(n, k+1)
        res += (n * (n - 1)) // ((k + 1) * k)
    
    # Return the final result
    return res

# Test the function with the provided test case
assert sum_Of_product(3) == 15