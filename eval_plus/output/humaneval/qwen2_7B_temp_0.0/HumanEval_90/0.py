
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
    This function finds the second smallest element in a list of integers.
    It returns None if there is no such element.
    """
    unique_elements = set(lst)
    if len(unique_elements) < 2:
        return None
    sorted_elements = sorted(unique_elements)
    return sorted_elements[1]

# Test cases to verify the correctness of the function
assert next_smallest([1, 2, 3, 4, 5]) == 2
assert next_smallest([5, 1, 4, 3, 2]) == 2
assert next_smallest([]) == None
assert next_smallest([1, 1]) == None
