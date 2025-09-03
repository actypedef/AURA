"""
Write a function to find the Eulerian number a(n, m).
assert eulerian_num(3, 1) == 4
"""
def eulerian_num(n, m):
    if n < m or m < 0 or n < 0:
        return 0
    if n == 0 or m == 0:
        return 1
    if m == 1:
        return n + 1
    if m == 2:
        return 2 * (n - 1)
    if m > 2:
        return (m - 1) * (eulerian_num(n - 1, m - 1) + eulerian_num(n - 1, m))

# Test cases
assert eulerian_num(3, 1) == 4