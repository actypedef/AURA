
def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    '''
from typing import *
from collections import *

def search(lst):
    # Create a frequency dictionary for the list
    freq = Counter(lst)
    
    # Initialize the result as -1
    result = -1
    
    # Iterate through the frequency dictionary
    for num, count in freq.items():
        # Check if the frequency is greater than or equal to the number itself
        if count >= num:
            # Update the result with the maximum number that satisfies the condition
            result = max(result, num)
    
    return result

# Test cases