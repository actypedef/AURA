"""
Write a function which returns nth catalan number.
assert catalan_number(10)==16796
"""
def catalan_number(n):
    # Initialize a list to store Catalan numbers
    catalan = [0] * (n + 1)
    
    # Base case: C(0) = 1
    catalan[0] = 1
    
    # Calculate each Catalan number using the formula
    for i in range(1, n + 1):
        catalan[i] = sum(catalan[j] * catalan[i - j - 1] for j in range(i))
    
    return catalan[n]

# Test the function with the provided test case
assert catalan_number(10) == 16796