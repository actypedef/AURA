"""
Write a function to find the length of the longest palindromic subsequence in the given string.
assert lps("TENS FOR TENS") == 5
"""
def lps(s):
    # Get the length of the input string
    n = len(s)
    
    # Create a 2D array to store lengths of longest palindromic subsequences
    dp = [[0 for x in range(n)] for y in range(n)]
    
    # All substrings of length 1 are palindromes
    for i in range(n):
        dp[i][i] = 1
    
    # Build the table from bottom up
    for cl in range(2, n + 1):  # cl is length of substring
        for i in range(n - cl + 1):
            j = i + cl - 1
            if s[i] == s[j] and cl == 2:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
    
    # The value in dp[0][n-1] will be the length of the longest palindromic subsequence
    return dp[0][n - 1]

# Test the function with the provided test case
assert lps("TENS FOR TENS") == 5