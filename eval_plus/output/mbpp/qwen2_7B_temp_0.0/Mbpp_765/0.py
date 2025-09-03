"""
Write a function to find nth polite number. geeksforgeeks.org/n-th-polite-number/
assert is_polite(7) == 11
"""
def is_polite(n):
    # Initialize an array to store polite numbers
    polite = [0] * (n + 1)
    
    # Base case: 0th polite number is 0
    polite[0] = 0
    
    # Calculate polite numbers up to n
    for i in range(1, n + 1):
        polite[i] = polite[i - 1] + 2
    
    # Return the nth polite number
    return polite[n]

# Test the function with the provided test case
assert is_polite(7) == 11
