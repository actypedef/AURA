"""
Write a function to find the nth jacobsthal number. https://www.geeksforgeeks.org/jacobsthal-and-jacobsthal-lucas-numbers/ 0, 1, 1, 3, 5, 11, 21, 43, 85, 171, 341, 683, 1365, 2731, ...
assert jacobsthal_num(5) == 11
"""
def jacobsthal_num(n):
    # Base cases for n = 0 and n = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Initialize the first two Jacobsthal numbers
    prev, curr = 0, 1
    
    # Calculate Jacobsthal numbers from n=2 onwards
    for _ in range(2, n + 1):
        next_val = 2 * curr + prev
        prev, curr = curr, next_val
    
    return curr

# Test the function with the provided test case
assert jacobsthal_num(5) == 11
