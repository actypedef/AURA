"""
Write a function to find the nth number in the newman conway sequence.
assert sequence(10) == 6
"""
def sequence(n):
    # Base cases for the Newman-Conway Sequence
    if n == 1 or n == 2:
        return 1
    
    # Initialize an array to store the sequence values
    f = [0] * (n + 1)
    
    # Set the first two elements of the sequence
    f[1], f[2] = 1, 1
    
    # Compute the rest of the sequence using the recurrence relation
    for i in range(3, n + 1):
        f[i] = f[f[i - 1]] + f[i - f[i - 1]]
    
    # Return the nth element of the sequence
    return f[n]

# Test the function with the provided test case
assert sequence(10) == 6