"""
Write a function to multiply two integers.
assert multiply_int(10,20)==200
"""
def multiply_int(a, b):
    return a * b

# Test cases to verify the correctness of the function
assert multiply_int(10, 20) == 200
assert multiply_int(5, 7) == 35
assert multiply_int(-1, 4) == -4
assert multiply_int(0, 10) == 0