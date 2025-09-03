"""
Write a function to find the nth nonagonal number.
assert is_nonagonal(10) == 325
"""
def is_nonagonal(n):
    # Calculate the formula for the nth nonagonal number
    return (7 * n**2 - 4) // 2

# Test cases to verify the correctness of the function
assert is_nonagonal(10) == 325
assert is_nonagonal(1) == 1
assert is_nonagonal(8) == 169
assert is_nonagonal(15) == 1225
assert is_nonagonal(20) == 2875