"""
Write a python function to find the highest power of 2 that is less than or equal to n.
assert highest_Power_of_2(10) == 8
"""
def highest_Power_of_2(n):
    # Initialize result to store the highest power of 2 less than or equal to n
    res = 0
    
    # Loop until n becomes 0
    while (n != 0):
        # Right shift n by 1 bit to divide it by 2
        n = n >> 1
        # Left shift res by 1 bit to multiply it by 2
        res = res << 1
    
    # Return the result which is the highest power of 2 <= n
    return res

# Test the function with the provided test case
assert highest_Power_of_2(10) == 8