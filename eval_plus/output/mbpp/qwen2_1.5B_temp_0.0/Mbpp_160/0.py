"""
Write a function that returns integers x and y that satisfy ax + by = n as a tuple, or return None if no solution exists.
assert find_solution(2, 3, 7) == (2, 1)
"""
def find_solution(a, b, n):
    # Check if there is a solution using the Extended Euclidean Algorithm
    gcd, x, y = extended_gcd(a, b)
    
    # If gcd is not 1, no solution exists
    if gcd != 1:
        return None
    
    # Calculate the coefficients of x and y
    x = x * (n // gcd)
    y = y * (n // gcd)
    
    # Ensure x and y are positive
    if x < 0:
        x += b
    if y < 0:
        y += a
    
    return (x, y)

# Helper function to calculate the greatest common divisor and coefficients
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

# Test cases
assert find_solution(2, 3, 7) == (2, 1)
assert find_solution(5, 4, 9) == (1, 2)
assert find_solution(6, 8, 10) == (1, 1)
assert find_solution(10, 12, 15) == (3, 1)
assert find_solution(11, 13, 145) == (1, 1)
assert find_solution(17, 23, 345) == (1, 1)
assert find_solution(19, 20, 345) == (1, 1)
assert find_solution(21, 22, 345) == (1, 1)
assert find_solution(23, 24, 345) == (1, 1)
assert find_solution(25, 26, 345) == (1, 1)
assert find_solution(27, 28, 345) == (1, 1)
assert find_solution(29, 30, 345) == (1, 1)
assert find_solution(31, 32, 345) == (1, 1)
assert find_solution(33, 34, 345) == (1, 1)
assert find_solution(35, 36, 345) == (1, 1)
assert find_solution(37, 38, 345) == (1, 1)
assert find_solution(39, 40, 345) == (1, 1)
assert find_solution(41, 42, 345) == (1, 1)
assert find_solution(43, 44, 345) == (1, 1)
assert find_solution(45, 46, 345) == (1, 1)
assert find_solution(47, 48, 345) == (1, 1)
assert find_solution(49, 50, 345) == (1, 1)
assert find_solution(51, 52, 345) == (1, 1)
assert find_solution(53, 54, 345) == (1, 1)
assert find_solution