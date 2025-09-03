"""
Write a function to find the maximum sum possible by using the given equation f(n) = max( (f(n/2) + f(n/3) + f(n/4) + f(n/5)), n).
assert get_max_sum(60) == 106
"""
def get_max_sum(n):
    # Initialize a dictionary to store computed values
    dp = {}
    
    def helper(x):
        # Check if the value has already been computed
        if x in dp:
            return dp[x]
        
        # Base case: if x is less than or equal to 1, return x
        if x <= 1:
            dp[x] = x
            return x
        
        # Recursively calculate the maximum sum for x
        dp[x] = max(helper(x // 2) + helper(x // 3) + helper(x // 4) + helper(x // 5), x)
        return dp[x]
    
    # Call the helper function with the input n
    return helper(n)

# Test the function with the provided test case
assert get_max_sum(60) == 106