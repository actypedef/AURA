"""
Write a function to find the nth number in the newman conway sequence.
assert sequence(10) == 6
"""
def sequence(n):
    # Initialize the first two numbers of the Newman Conway sequence
    seq = [0, 1]
    
    # Generate the sequence up to the nth number
    while len(seq) < n + 1:
        next_num = seq[-1] + seq[-2]
        seq.append(next_num)
    
    return seq[n]

# Test cases to verify the correctness of the solution
assert sequence(10) == 6
assert sequence(5) == 3
assert sequence(8) == 4
assert sequence(1) == 1
assert sequence(0) == 0