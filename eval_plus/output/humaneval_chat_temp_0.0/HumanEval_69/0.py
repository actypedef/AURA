
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
from collections import Counter

def search(lst):
    """
    Finds the greatest integer in the list whose frequency is greater than or equal to its value.

    :param lst: List of positive integers
    :return: The greatest integer meeting the criteria or -1 if no such integer exists
    """
    # Count the frequency of each number in the list
    freq = Counter(lst)
    
    # Initialize the result as -1 (default if no valid number is found)
    result = -1
    
    # Iterate through the items in the frequency dictionary
    for num, count in freq.items():
        # Check if the number's frequency is at least as large as the number itself
        if num <= count:
            # Update the result with the maximum of the current result and the number
            result = max(result, num)
    
    return result

# Test cases to verify the correctness of the function
assert search([4, 1, 2, 2, 3, 1]) == 2
assert search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
assert search([5, 5, 4, 4, 4]) == -1