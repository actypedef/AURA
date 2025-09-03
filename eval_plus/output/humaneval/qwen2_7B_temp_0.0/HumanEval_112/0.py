
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
# Import necessary packages
from typing import Tuple

def reverse_delete(s: str, c: str) -> Tuple[str, bool]:
    """
    Deletes all characters in 's' that are present in 'c' and checks if the resulting string is a palindrome.
    
    Parameters:
    - s (str): The original string from which characters will be removed.
    - c (str): The string containing characters to remove from 's'.
    
    Returns:
    - Tuple[str, bool]: A tuple containing the modified string and a boolean indicating whether it's a palindrome.
    """
    # Remove characters from 's' that are present in 'c'
    result = ''.join([char for char in s if char not in c])
    
    # Check if the result string is a palindrome
    is_palindrome = result == result[::-1]
    
    return (result, is_palindrome)

# Function to test the correctness of the solution
def check_solution():
    assert reverse_delete("abcde", "ae") == ('bcd', False), "Test case 1 failed"
    assert reverse_delete("abcdef", "b") == ('acdef', False), "Test case 2 failed"
    assert reverse_delete("abcdedcba", "ab") == ('cdedc', True), "Test case 3 failed"

# Run the test function
check_solution()