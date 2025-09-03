
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
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    >>> strange_sort_list([1, 2, 3, 4])
    [1, 4, 2, 3]
    >>> strange_sort_list([5, 5, 5, 5])
    [5, 5, 5, 5]
    >>> strange_sort_list([])
    []
    """
    # Sort the list to get the minimum and maximum values
    sorted_lst = sorted(lst)
    
    # Initialize two pointers for the start and end of the sorted list
    start = 0
    end = len(sorted_lst) - 1
    
    # Use a loop to alternate between adding the minimum and maximum values
    result = []
    while start <= end:
        if start == end:
            result.append(sorted_lst[start])
            break
        result.append(sorted_lst[start])
        result.append(sorted_lst[end])
        start += 1
        end -= 1
    
    return result

# Test cases to verify the correctness of the function
assert strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
assert strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
assert strange_sort_list([]) == []