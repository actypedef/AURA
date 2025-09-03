
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
    # Check if the list is empty or contains a single element
    if len(lst) <= 1:
        return True
    
    # Initialize previous number to the first element
    prev = lst[0]
    
    # Iterate through the list starting from the second element
    for num in lst[1:]:
        # Check if current number is less than the previous one (not sorted)
        if num < prev:
            return False
        
        # Check for duplicates
        if num == prev:
            return False
        
        # Update previous number
        prev = num
    
    # If all checks pass, the list is sorted
    return True

# Test cases