"""
Write a function to find the nth number in the newman conway sequence.
assert sequence(10) == 6
"""
def sequence(n):
    # Base cases for the Newman-Conway Sequence
    if n == 1 or n == 2:
        return 1
    
    # Initialize an array to store computed values of the sequence
    arr = [0] * (n + 1)
    
    # Set initial values
    arr[1], arr[2] = 1, 1
    
    # Compute the sequence iteratively
    for i in range(3, n + 1):
        arr[i] = arr[arr[i - 1]] + arr[i - arr[i - 1]]
    
    # Return the nth element of the sequence
    return arr[n]

# Test the function with the provided test case
assert sequence(10) == 6