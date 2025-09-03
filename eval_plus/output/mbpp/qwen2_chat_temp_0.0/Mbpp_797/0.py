"""
Write a python function to find the sum of all odd natural numbers within the range l and r.
assert sum_in_range(2,5) == 8
"""
def sum_in_range(l, r):
    # Calculate the sum of all odd numbers between l and r (inclusive)
    return ((r + 1) // 2 - (l - 1) // 2) * ((r + 1) % 2 + (l - 1) % 2)

# Test the function with the provided test case
assert sum_in_range(2, 5) == 8