"""
Write a function to check whether the given number is a perfect square or not. https://www.geeksforgeeks.org/check-if-given-number-is-perfect-square-in-cpp/
assert not is_perfect_square(10)
"""
def is_perfect_square(n):
    # Check if the input number is less than 2
    if n < 2:
        return False
    
    # Calculate the integer part of the square root of n
    x = int(n ** 0.5)
    
    # Check if the square of x equals n
    if x * x == n:
        return True
    else:
        return False

# Test the function with the provided test case
assert not is_perfect_square(10)
