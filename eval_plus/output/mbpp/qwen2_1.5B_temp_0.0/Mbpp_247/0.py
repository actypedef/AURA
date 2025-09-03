"""
Write a function to find the length of the longest palindromic subsequence in the given string.
assert lps("TENS FOR TENS") == 5
"""
def lps(s):
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    
    # All substrings of length 1 are palindromes
    for i in range(n):
        dp[i][i] = 1
    
    # Check for lengths greater than 2
    for length in range(2, n + 1):
        for start in range(n - length + 1):
            end = start + length - 1
            if s[start] == s[end]:
                dp[start][end] = dp[start + 1][end - 1] + 2
            else:
                dp[start][end] = max(dp[start + 1][end], dp[start][end - 1])
    
    return dp[0][n - 1]

# Test cases
assert lps("TENS FOR TENS") == 5
assert lps("BANANA") == 3
assert lps("CIVIC") == 5
assert lps("") == 0
assert lps("A") == 1