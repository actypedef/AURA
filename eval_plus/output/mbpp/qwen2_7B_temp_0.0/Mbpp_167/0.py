"""
Write a python function to find the smallest power of 2 greater than or equal to n.
assert next_power_of_2(0) == 1
"""
def next_power_of_2(n):
    # If n is less than or equal to 0, return 1 as the smallest power of 2
    if n <= 0:
        return 1
    
    # Initialize p to 2 (the smallest power of 2)
    p = 2
    
    # Loop until p is greater than or equal to n
    while p < n:
        p *= 2
    
    # Return the found power of 2
    return p

# Test cases to validate the function
assert next_power_of_2(0) == 1