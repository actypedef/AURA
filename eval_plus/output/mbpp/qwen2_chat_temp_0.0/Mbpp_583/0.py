"""
Write a function which returns nth catalan number.
assert catalan_number(10)==16796
"""
def catalan_number(n):
    # Initialize an array to store the Catalan numbers up to n
    C = [0] * (n + 1)
    
    # Base cases for the first two Catalan numbers
    C[0] = 1
    if n > 0:
        C[1] = 1
    
    # Calculate the remaining Catalan numbers using the recursive formula
    for i in range(2, n + 1):
        for j in range(i):
            C[i] += C[j] * C[i - j - 1]
    
    # Return the nth Catalan number
    return C[n]

# Test the function with the provided test case
assert catalan_number(10) == 16796
