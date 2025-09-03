"""
Write a function to check whether the given number is a perfect square or not. https://www.geeksforgeeks.org/check-if-given-number-is-perfect-square-in-cpp/
assert not is_perfect_square(10)
"""
import math

def is_perfect_square(n):
    # Calculate the square root of the number
    sqrt_n = int(math.sqrt(n))
    
    # Check if the square of the integer square root equals the original number
    return sqrt_n * sqrt_n == n

# Test the function with the provided test case
assert not is_perfect_square(10)
