"""
Write a function to find the number of ways to partition a set of Bell numbers.
assert bell_number(2)==2
"""
def bell_number(n):
    # Initialize a list to store Bell numbers
    bell = [0] * (n + 1)
    bell[0] = 1
    
    # Fill the Bell numbers using previously computed values
    for i in range(1, n + 1):
        bell[i] = bell[i - 1]
        for j in range(1, i + 1):
            bell[i] += bell[j - 1]
    
    return bell[n]

# Test the function with the provided test case
assert bell_number(2) == 2