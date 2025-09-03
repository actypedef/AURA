"""
Write a python function to find the smallest power of 2 greater than or equal to n.
assert next_power_of_2(0) == 1
"""
def next_power_of_2(n):
    # If n is less than or equal to 0, return 1 as the smallest power of 2
    if n <= 0:
        return 1
    
    # Decrement n to handle cases where n is already a power of 2
    n -= 1
    
    # Set all bits after the rightmost set bit
    n |= n >> 1
    n |= n >> 2
    n |= n >> 4
    n |= n >> 8
    n |= n >> 16
    
    # Increment n to get the next power of 2
    return n + 1

# Test the function with the provided test case
assert next_power_of_2(0) == 1
