"""
Write a python function to find the sum of even factors of a number.
assert sumofFactors(18) == 26
"""
import math 

def sumofFactors(n): 
    # Initialize the sum of factors to 0
    res = 0
    
    # Iterate through all numbers from 1 to sqrt(n)
    for i in range(1, int(math.sqrt(n)) + 2): 
        if n % i == 0: 
            # If i is a factor, check if it is even
            if i % 2 == 0: 
                res += i 
            # Check if the corresponding factor (n // i) is different and even
            if (n // i != i) and ((n // i) % 2 == 0): 
                res += (n // i) 
    
    return res 

# Test the function with the provided test case
assert sumofFactors(18) == 26
