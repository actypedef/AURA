"""
Write a function to find the number of ways to partition a set of Bell numbers.
assert bell_number(2)==2
"""
def bell_number(n):
    # Initialize a list to store Bell numbers up to n
    B = [0] * (n + 1)
    
    # Base case: Bell number for 0 is 1
    B[0] = 1
    
    # Compute Bell numbers using the recursive relation
    for i in range(1, n + 1):
        B[i] = sum(B[j] * binomial_coefficient(i - 1, j) for j in range(i))
    
    return B[n]

# Function to calculate binomial coefficient C(n, k)
def binomial_coefficient(n, k):
    res = 1
    if k > n / 2:
        k = n - k
    for i in range(k):
        res *= (n - i)
        res //= (i + 1)
    return res

# Test the function with the provided test case
assert bell_number(2) == 2