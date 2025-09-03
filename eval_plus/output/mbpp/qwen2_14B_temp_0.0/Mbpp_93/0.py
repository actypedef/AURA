"""
Write a function to calculate the value of 'a' to the power 'b'.
assert power(3,4) == 81
"""
def power(a, b):
    # Base case: any number raised to the power of 0 is 1
    if b == 0:
        return 1
    else:
        # Recursive case: multiply 'a' by the result of 'a' raised to the power of (b-1)
        return a * power(a, b - 1)

# Test the function with the provided test case
assert power(3, 4) == 81
