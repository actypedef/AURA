
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
def can_arrange(arr):
    """
    Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] < arr[i - 1]:
            return i
    return -1

# Test cases
assert can_arrange([1, 2, 4, 3, 5]) == 3
assert can_arrange([1, 2, 3]) == -1
assert can_arrange([5, 4, 3, 2, 1]) == 1
assert can_arrange([1, 2, 3, 4, 5]) == -1
assert can_arrange([1, 3, 2, 4, 5]) == 2
assert can_arrange([1, 2, 3, 4, 5, 6]) == -1
assert can_arrange([1, 2, 3, 4, 5, 6, 7]) == -1
assert can_arrange([1, 2, 3, 4, 5, 6, 7, 8]) == -1
assert can_arrange([1, 2, 3, 4, 5, 6, 7, 8, 9]) == -1
assert can_arrange([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1
assert can_arrange([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == -1
assert can_arrange([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == -1
assert can_arrange([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == -1
assert can_arrange([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == -1
assert can_arrange([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == -1
assert can_arrange([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == -1
assert can_arrange([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,