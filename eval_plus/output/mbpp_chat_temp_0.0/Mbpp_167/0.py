"""
Write a python function to find the smallest power of 2 greater than or equal to n.
assert next_power_of_2(0) == 1
"""
def next_power_of_2(n):
    # If n is less than or equal to 0, return 1 as the smallest power of 2
    if (n <= 0):
        return 1
    
    # Initialize p to 1 which will be used to calculate powers of 2
    p = 1
    
    # Loop until p is greater than or equal to n
    while (p < n):
        # Double the value of p in each iteration
        p *= 2
    
    # Return the calculated power of 2
    return p

# Test the function with the provided test case
assert next_power_of_2(0) == 1
