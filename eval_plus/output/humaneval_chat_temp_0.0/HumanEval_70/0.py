
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
    Sorts a given list of integers in a 'strange' order: starting with the minimum value,
    then the maximum of the remaining integers, then the next minimum, and so on.

    :param lst: List of integers to be sorted.
    :return: A new list of integers sorted in the described 'strange' order.
    """
    # Create a copy of the list to avoid modifying the original list
    sorted_lst = lst[:]
    # Initialize an empty list to store the result
    result = []
    # Loop until the sorted list is empty
    while sorted_lst:
        # Append the minimum value from the sorted list
        result.append(min(sorted_lst))
        # Remove the minimum value from the sorted list
        sorted_lst.remove(min(sorted_lst))
        # If the sorted list is not empty, append the maximum value
        if sorted_lst:
            result.append(max(sorted_lst))
            # Remove the maximum value from the sorted list
            sorted_lst.remove(max(sorted_lst))
    return result

# Test cases to verify the correctness of the function
assert strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3], "Test case 1 failed"
assert strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5], "Test case 2 failed"
assert strange_sort_list([]) == [], "Test case 3 failed"
