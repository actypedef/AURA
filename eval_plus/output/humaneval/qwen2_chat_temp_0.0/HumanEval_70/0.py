
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
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    """
    sorted_lst = sorted(lst)
    result = []
    while sorted_lst:
        if len(sorted_lst) % 2 == 0:
            result.append(sorted_lst.pop(0))
        else:
            result.append(sorted_lst.pop())
    return result

# Check function to verify the correctness of the solution
def check_strange_sort():
    assert strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3], "Test case 1 failed"
    assert strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5], "Test case 2 failed"
    assert strange_sort_list([]) == [], "Test case 3 failed"
    print("All test cases passed!")

check_strange_sort()