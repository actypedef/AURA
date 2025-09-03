"""
Write a function to find the Eulerian number a(n, m).
assert eulerian_num(3, 1) == 4
"""
def eulerian_num(n, m):
    # Base case: If n equals m or n equals 0, return 1
    if (n == m) or (n == 0):
        return 1
    
    # Base case: If m is greater than or equal to n, return 0
    if m >= n:
        return 0
    
    # Recursive relation for Eulerian numbers
    return ((m + 1) * eulerian_num(n - 1, m - 1)) + (n - m) * eulerian_num(n - 1, m)

# Test the function with the provided test case
assert eulerian_num(3, 1) == 4
