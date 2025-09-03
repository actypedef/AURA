"""
Write a function to find the Eulerian number a(n, m).
assert eulerian_num(3, 1) == 4
"""
def eulerian_num(n, m):
    # Base case: If n is greater than m, return 0
    if n > m + 1:
        return 0
    # Base case: If m is 0, return 1
    if m == 0:
        return 1
    # Recursive formula to calculate Eulerian number
    return ((n - m) * eulerian_num(n - 1, m - 1) + (m + 1) * eulerian_num(n - 1, m))

# Test the function with the provided test case
assert eulerian_num(3, 1) == 4
