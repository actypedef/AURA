
def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''
def strange_sort_list(lst):
    """
    Sorts a list of integers in a strange order: starting with the minimum value,
    then the maximum of the remaining integers, then the minimum again, and so on.
    
    :param lst: List of integers to be sorted
    :return: A new list sorted in the described strange order
    
    Examples:
    >>> strange_sort_list([1, 2, 3, 4])
    [1, 4, 2, 3]
    >>> strange_sort_list([5, 5, 5, 5])
    [5, 5, 5, 5]
    >>> strange_sort_list([])
    []
    """
    # Create a copy of the list to avoid modifying the original list
    temp_lst = lst[:]
    result = []
    while temp_lst:
        # Append the minimum value
        min_val = min(temp_lst)
        result.append(min_val)
        temp_lst.remove(min_val)
        
        if temp_lst:
            # Append the maximum value if there are still elements left
            max_val = max(temp_lst)
            result.append(max_val)
            temp_lst.remove(max_val)
    return result

# Check function to verify the correctness of the solution
def check():
    assert strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3], "Test case 1 failed"
    assert strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5], "Test case 2 failed"
    assert strange_sort_list([]) == [], "Test case 3 failed"

check()