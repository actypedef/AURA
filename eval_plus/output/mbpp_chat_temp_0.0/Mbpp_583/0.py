"""
Write a function which returns nth catalan number.
assert catalan_number(10)==16796
"""
def catalan_number(n):
    # Base case: the first Catalan number is 1
    if n == 0:
        return 1
    
    # Initialize an array to store intermediate results
    C = [0] * (n + 1)
    
    # The first Catalan number is 1
    C[0] = 1
    
    # Calculate each Catalan number using the previous values
    for i in range(1, n + 1):
        for j in range(i):
            C[i] += C[j] * C[i - j - 1]
    
    # Return the nth Catalan number
    return C[n]

# Test the function with the provided test case
assert catalan_number(10) == 16796