"""
Write a function which returns nth catalan number.
assert catalan_number(10)==16796
"""
import math 

def catalan_number(num): 
    # Calculate the nth Catalan number using the formula
    return math.factorial(2 * num) // (math.factorial(num + 1) * math.factorial(num)) 

# Test the function with the provided test case
assert catalan_number(10) == 16796
