"""
Write a function to find the nth jacobsthal number. https://www.geeksforgeeks.org/jacobsthal-and-jacobsthal-lucas-numbers/ 0, 1, 1, 3, 5, 11, 21, 43, 85, 171, 341, 683, 1365, 2731, ...
assert jacobsthal_num(5) == 11
"""
def jacobsthal_num(n):
    # Base case: if n is 0, return 0
    if n == 0:
        return 0
    # Initialize an array to store Jacobsthal numbers up to n
    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 1
    
    # Fill the array using the recurrence relation J(n) = J(n-1) + 2*J(n-2)
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 2 * dp[i - 2]
    
    # Return the nth Jacobsthal number
    return dp[n]

# Test the function with the provided test case
assert jacobsthal_num(5) == 11