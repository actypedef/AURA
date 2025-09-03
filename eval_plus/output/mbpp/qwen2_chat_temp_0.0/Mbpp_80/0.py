"""
Write a function to find the nth tetrahedral number.
assert tetrahedral_number(5) == 35
"""
def tetrahedral_number(n):
    # Calculate the nth tetrahedral number using the formula n*(n+1)*(n+2)/6
    return int(n * (n + 1) * (n + 2) / 6)

# Test the function with the provided test case
assert tetrahedral_number(5) == 35
