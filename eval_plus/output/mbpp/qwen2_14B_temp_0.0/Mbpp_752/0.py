"""
Write a function to find the nth jacobsthal number. https://www.geeksforgeeks.org/jacobsthal-and-jacobsthal-lucas-numbers/ 0, 1, 1, 3, 5, 11, 21, 43, 85, 171, 341, 683, 1365, 2731, ...
assert jacobsthal_num(5) == 11
"""
def jacobsthal_num(n):
    # Base cases for the first two Jacobsthal numbers
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Initialize the first two Jacobsthal numbers
    a = 0
    b = 1
    
    # Compute the Jacobsthal numbers iteratively up to the nth number
    for i in range(2, n + 1):
        c = a + 2 * b
        a = b
        b = c
    
    return b

# Test the function with the provided test case
assert jacobsthal_num(5) == 11
