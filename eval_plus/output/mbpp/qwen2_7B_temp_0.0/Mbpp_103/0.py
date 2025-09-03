"""
Write a function to find the Eulerian number a(n, m).
assert eulerian_num(3, 1) == 4
"""
def eulerian_num(n, m):
    # Base case: If n equals m, return 1
    if n == m:
        return 1
    # Base case: If n is 0 or m is greater than n, return 0
    elif n == 0 or m > n:
        return 0
    else:
        # Recursive relation for Eulerian numbers
        return ((n - m) * eulerian_num(n - 1, m - 1)) + (m + 1) * eulerian_num(n - 1, m)

# Test the function with the provided test case
assert eulerian_num(3, 1) == 4