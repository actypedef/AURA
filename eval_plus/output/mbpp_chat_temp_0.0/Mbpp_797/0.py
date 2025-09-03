"""
Write a python function to find the sum of all odd natural numbers within the range l and r.
assert sum_in_range(2,5) == 8
"""
def sum_in_range(l, r):
    # Calculate the number of odd numbers between l and r (inclusive)
    n = ((r - l) // 2) + 1
    
    # If l is even, adjust it to the next odd number
    if l % 2 == 0:
        l += 1
    
    # Calculate the sum of the first n odd numbers starting from l
    return int(n * (l + l + 2 * (n - 1)) / 2)

# Test the function with the provided test case
assert sum_in_range(2, 5) == 8