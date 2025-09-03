
def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Examples
    is_sorted([5]) ➞ True
    is_sorted([1, 2, 3, 4, 5]) ➞ True
    is_sorted([1, 3, 2, 4, 5]) ➞ False
    is_sorted([1, 2, 3, 4, 5, 6]) ➞ True
    is_sorted([1, 2, 3, 4, 5, 6, 7]) ➞ True
    is_sorted([1, 3, 2, 4, 5, 6, 7]) ➞ False
    is_sorted([1, 2, 2, 3, 3, 4]) ➞ True
    is_sorted([1, 2, 2, 2, 3, 4]) ➞ False
    '''
def is_sorted(lst):
    # Check if the list is empty or contains a single element, which is considered sorted
    if len(lst) <= 1:
        return True
    
    # Iterate through the list to check for sorting and duplicates
    for i in range(1, len(lst)):
        # Check if the current element is less than the previous one (not sorted)
        if lst[i] < lst[i - 1]:
            return False
        
        # Check for more than one duplicate of the same number
        if i > 1 and lst[i] == lst[i - 1] == lst[i - 2]:
            return False
    
    # If all checks pass, the list is sorted
    return True

# Test cases