"""
Write a function to find the n'th lucas number.
assert find_lucas(9) == 76
"""
def find_lucas(n):
    # Base case: if n is 0, return 2 (first lucas number)
    if n == 0:
        return 2
    # Base case: if n is 1, return 1 (second lucas number)
    elif n == 1:
        return 1
    else:
        # Recursive call to calculate the nth lucas number using the formula L(n) = L(n-1) + L(n-2)
        return find_lucas(n - 1) + find_lucas(n - 2)

# Test the function with the provided test case
assert find_lucas(9) == 76
