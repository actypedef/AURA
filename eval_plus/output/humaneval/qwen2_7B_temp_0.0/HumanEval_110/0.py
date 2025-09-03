
def exchange(lst1, lst2):
    """In this problem, you will implement a function that takes two lists of numbers,
    and determines whether it is possible to perform an exchange of elements
    between them to make lst1 a list of only even numbers.
    There is no limit on the number of exchanged elements between lst1 and lst2.
    If it is possible to exchange elements between the lst1 and lst2 to make
    all the elements of lst1 to be even, return "YES".
    Otherwise, return "NO".
    For example:
    exchange([1, 2, 3, 4], [1, 2, 3, 4]) => "YES"
    exchange([1, 2, 3, 4], [1, 5, 3, 4]) => "NO"
    It is assumed that the input lists will be non-empty.
    """
# Import necessary packages
from typing import List

def can_make_even(lst1: List[int], lst2: List[int]) -> str:
    """
    Determines if it's possible to exchange elements between two lists to make the first list consist only of even numbers.
    
    Parameters:
    lst1 (List[int]): The first list of integers.
    lst2 (List[int]): The second list of integers.
    
    Returns:
    str: "YES" if it's possible to make all elements in lst1 even through exchanges, otherwise "NO".
    """
    # Count odd numbers in lst1 and even numbers in lst2
    odd_count = sum(1 for x in lst1 if x % 2 != 0)
    even_count = sum(1 for x in lst2 if x % 2 == 0)
    
    # Check if there are enough even numbers in lst2 to exchange with odd numbers in lst1
    if even_count >= odd_count:
        return "YES"
    else:
        return "NO"

# Test cases to verify the correctness of the function
assert can_make_even([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"
assert can_make_even([1, 2, 3, 4], [1, 5, 3, 4]) == "NO"