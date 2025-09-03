"""
Write a function to find the nth number in the newman conway sequence.
assert sequence(10) == 6
"""
def sequence(n):
    # Initialize a list to store the Newman-Conway sequence values
    seq = [0] * (n + 1)
    
    # Base cases
    seq[1] = 1
    
    # Generate the sequence up to the nth number
    for i in range(2, n + 1):
        seq[i] = seq[seq[i - 1]] + seq[i - seq[i - 1]]
    
    # Return the nth number in the sequence
    return seq[n]

# Test the function with the provided test case
assert sequence(10) == 6
