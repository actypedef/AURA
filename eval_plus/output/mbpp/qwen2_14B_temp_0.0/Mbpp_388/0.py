"""
Write a python function to find the highest power of 2 that is less than or equal to n.
assert highest_Power_of_2(10) == 8
"""
import math

def highest_power_of_2(n):
    # Calculate the highest power of 2 less than or equal to n
    return int(math.pow(2, math.floor(math.log(n, 2))))

# Test the function with the provided test case
assert highest_power_of_2(10) == 8
