
def reverse_delete(s,c):
    """Task
    We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    Example
    For s = "abcde", c = "ae", the result should be ('bcd',False)
    For s = "abcdef", c = "b"  the result should be ('acdef',False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc',True)
    """
def reverse_delete(s, c):
    # Reverse the original string
    reversed_s = s[::-1]
    
    # Create a new string without characters from 'c'
    filtered_s = ''.join([char for char in reversed_s if char not in c])
    
    # Check if the filtered string is a palindrome
    is_palindrome = filtered_s == filtered_s[::-1]
    
    return (filtered_s, is_palindrome)

# Test cases
assert reverse_delete("abcde", "ae") == ('bcd', False)
assert reverse_delete("abcdef", "b") == ('acdef', False)
assert reverse_delete("abcdedcba", "ab") == ('cdedc', True)