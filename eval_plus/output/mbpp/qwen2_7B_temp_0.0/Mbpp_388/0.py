"""
Write a python function to find the highest power of 2 that is less than or equal to n.
assert highest_Power_of_2(10) == 8
"""
def highest_Power_of_2(n):
    # Initialize result as 1, which is the smallest power of 2
    res = 1
    
    # Loop until the result becomes greater than n
    while (res * 2 <= n):
        res *= 2
    
    # Return the highest power of 2 found
    return res

# Test the function with the provided test case
assert highest_Power_of_2(10) == 8