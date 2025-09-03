"""
Write a function that returns integers x and y that satisfy ax + by = n as a tuple, or return None if no solution exists.
assert find_solution(2, 3, 7) == (2, 1)
"""
def find_solution(a, b, n):
    # Iterate through possible values of x starting from 0
    for x in range(n // a + 1):
        # Calculate the remaining value after subtracting ax
        remaining = n - (a * x)
        # Check if the remaining value is divisible by b
        if remaining % b == 0:
            # If so, calculate y and return the tuple (x, y)
            y = remaining // b
            return (x, y)
    # If no solution is found, return None
    return None

# Test the function with the provided test case
assert find_solution(2, 3, 7) == (2, 1)
