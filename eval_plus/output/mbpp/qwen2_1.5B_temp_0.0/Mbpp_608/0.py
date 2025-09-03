"""
Write a python function to find nth bell number.
assert bell_Number(2) == 2
"""
def bell_number(n):
    if n == 0:
        return 1
    else:
        return sum(bell_number(k-1) * (n-k+1) for k in range(1, n+1))

# Test cases
assert bell_number(2) == 2
assert bell_number(3) == 5
assert bell_number(4) == 15
assert bell_number(5) == 52