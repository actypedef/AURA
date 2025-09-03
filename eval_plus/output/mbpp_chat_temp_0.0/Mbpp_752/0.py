"""
Write a function to find the nth jacobsthal number. https://www.geeksforgeeks.org/jacobsthal-and-jacobsthal-lucas-numbers/ 0, 1, 1, 3, 5, 11, 21, 43, 85, 171, 341, 683, 1365, 2731, ...
assert jacobsthal_num(5) == 11
"""
def jacobsthal_num(n):
    # Base case: if n is 0, return 0
    if n == 0:
        return 0
    # Base case: if n is 1, return 1
    elif n == 1:
        return 1
    else:
        # Recursive relation for Jacobsthal numbers
        return (jacobsthal_num(n - 1) + 2 * jacobsthal_num(n - 2))

# Test the function with the provided test case
assert jacobsthal_num(5) == 11
