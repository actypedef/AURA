"""
Write a python function to find nth bell number.
assert bell_Number(2) == 2
"""
def bell_Number(n):
    # Initialize a list to store Bell numbers
    B = [0] * (n + 1)
    
    # Base case: Bell number for n=0 is 1
    B[0] = 1
    
    # Calculate Bell numbers using the formula
    for i in range(1, n + 1):
        B[i] = 0
        for j in range(i - 1, -1, -1):
            B[j] += B[j - 1]
    
    # Return the nth Bell number
    return B[n]

# Test the function with the provided test case
assert bell_Number(2) == 2