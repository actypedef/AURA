"""
Write a python function to find the smallest power of 2 greater than or equal to n.
assert next_power_of_2(0) == 1
"""
def next_power_of_2(n):
    # If n is less than or equal to 1, return 1 as it's the smallest power of 2
    if (n <= 1):
        return 1
    
    # Calculate the position of the most significant bit using log base 2
    p = int(math.log(n - 1, 2))
    
    # Return the power of 2 raised to the calculated position plus one
    return math.pow(2, p + 1)

# Test the function with the provided test case
assert next_power_of_2(0) == 1