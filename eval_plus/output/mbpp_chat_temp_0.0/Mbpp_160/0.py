"""
Write a function that returns integers x and y that satisfy ax + by = n as a tuple, or return None if no solution exists.
assert find_solution(2, 3, 7) == (2, 1)
"""
def find_solution(a, b, n):
    # Iterate over possible values of x from 0 to n//a
    for x in range(n // a + 1):
        # Calculate the remaining value after subtracting ax from n
        rem = n - (x * a)
        
        # Check if the remaining value is divisible by b
        if rem % b == 0:
            # If so, calculate y and return the tuple (x, y)
            y = rem // b
            return (x, y)
    
    # If no solution is found, return None
    return None

# Test the function with the provided test case
assert find_solution(2, 3, 7) == (2, 1)
