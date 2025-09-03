
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
    # Check if the list has less than 2 elements
    if len(lst) < 2:
        return None
    
    # Remove duplicates to ensure we find the second smallest unique number
    unique_lst = list(set(lst))
    
    # Sort the unique list
    sorted_lst = sorted(unique_lst)
    
    # Check if there is at least one more element after the first
    if len(sorted_lst) > 1:
        return sorted_lst[1]
    else:
        return None

# Test cases