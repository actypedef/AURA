"""
Write a function that returns integers x and y that satisfy ax + by = n as a tuple, or return None if no solution exists.
assert find_solution(2, 3, 7) == (2, 1)
"""
def find_solution(a, b, n):
    # Iterate through all possible values of x
    for x in range(n // a + 1):
        # Calculate the corresponding value of y
        y = (n - a * x) / b
        # Check if y is an integer
        if y.is_integer():
            return (x, int(y))
    # Return None if no solution is found
    return None

# Test the function with the provided test case
assert find_solution(2, 3, 7) == (2, 1)
