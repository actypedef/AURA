"""
Write a python function to find the sum of the product of consecutive binomial co-efficients.
assert sum_Of_product(3) == 15
"""
def sum_Of_product(n):
    # Initialize the result variable
    res = 0
    
    # Loop through each number from 2 to n+1
    for i in range(2, n + 2):
        # Calculate the product of binomial coefficients (i choose 1) * (i choose 2)
        res += i * (i - 1) // 2
    
    return res

# Test the function with the provided test case
assert sum_Of_product(3) == 15
