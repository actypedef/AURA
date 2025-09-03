"""
Write a function which returns nth catalan number.
assert catalan_number(10)==16796
"""
def catalan_number(n):
    # Base case: C(0) = 1
    if n == 0:
        return 1
    # Recursive case: C(n) = (2n-1) * C(n-1) / (n+1)
    else:
        return (2*n - 1) * catalan_number(n-1) // (n + 1)

# Test cases to verify the correctness of the function
assert catalan_number(10) == 16796
assert catalan_number(5) == 42
assert catalan_number(8) == 987