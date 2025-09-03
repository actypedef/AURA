"""
Write a function to calculate the value of 'a' to the power 'b'.
assert power(3,4) == 81
"""
def power(a, b):
    # Base case: any number to the power of 0 is 1
    if b == 0:
        return 1
    # Base case: 0 to the power of any positive number is 0
    elif a == 0:
        return 0
    # Base case: any number to the power of 1 is itself
    elif b == 1:
        return a
    # Recursive case: multiply 'a' by the result of 'a' raised to 'b-1'
    else:
        return a * power(a, b - 1)

# Test the function with the provided test case
assert power(3, 4) == 81
