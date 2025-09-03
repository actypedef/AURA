"""
Write a function to find the length of the longest palindromic subsequence in the given string.
assert lps("TENS FOR TENS") == 5
"""
def lps(s):
    # Get the length of the input string
    n = len(s)
    
    # Create a 2D array to store lengths of longest palindromic subsequences
    L = [[0 for x in range(n)]for y in range(n)]
    
    # Strings of length 1 are palindrome of length 1
    for i in range(n):
        L[i][i] = 1
    
    # Build the table. Note that the lower diagonal values of table are useless and not filled in the process. cl is length of substring
    for cl in range(2, n+1):
        for i in range(n-cl+1):
            j = i + cl - 1
            if s[i] == s[j] and cl == 2:
                L[i][j] = 2
            elif s[i] == s[j]:
                L[i][j] = L[i+1][j-1] + 2
            else:
                L[i][j] = max(L[i][j-1], L[i+1][j])
    
    # Length of the longest palindromic subsequnce is in L[0][n-1]
    return L[0][n-1]

# Test the function with the provided test case
assert lps("TENS FOR TENS") == 5