"""
Write a function to find the length of the longest palindromic subsequence in the given string.
assert lps("TENS FOR TENS") == 5
"""
def lps(s):
    # Initialize a matrix to store lengths of longest palindromic subsequences
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    
    # Every single character is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1
    
    # Fill the table
    for cl in range(2, n + 1):  # cl is the length of substring
        for i in range(n - cl + 1):
            j = i + cl - 1
            if s[i] == s[j] and cl == 2:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
    
    # The length of the longest palindromic subsequence will be in dp[0][n-1]
    return dp[0][n - 1]

# Test the function with the provided test case
assert lps("TENS FOR TENS") == 5
