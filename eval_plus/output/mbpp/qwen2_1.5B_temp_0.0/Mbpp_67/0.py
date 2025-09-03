"""
Write a function to find the number of ways to partition a set of Bell numbers.
assert bell_number(2)==2
"""
def bell_number(n):
    # Base case: B0 = 1
    if n == 0:
        return 1
    
    # Initialize the first two Bell numbers
    b = [0] * (n + 1)
    b[0], b[1] = 1, 1
    
    # Calculate Bell numbers using dynamic programming
    for i in range(2, n + 1):
        for j in range(i):
            b[i] += b[j] * b[i - j - 1]
    
    return b[n]

# Test cases to verify the correctness of the solution
assert bell_number(2) == 2
assert bell_number(3) == 5
assert bell_number(4) == 15
assert bell_number(5) == 52