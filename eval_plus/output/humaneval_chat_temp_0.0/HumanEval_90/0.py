
def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    """
def next_smallest(lst):
    """
    Returns the second smallest element in a list of integers.
    If there is no such element, returns None.
    """
    # Remove duplicates and sort the list
    unique_sorted_lst = sorted(set(lst))
    
    # Check if there are at least two unique elements
    if len(unique_sorted_lst) < 2:
        return None
    
    # Return the second smallest element
    return unique_sorted_lst[1]

# Test cases to verify the correctness of the function
assert next_smallest([1, 2, 3, 4, 5]) == 2
assert next_smallest([5, 1, 4, 3, 2]) == 2
assert next_smallest([]) == None
assert next_smallest([1, 1]) == None
