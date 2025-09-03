
def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    Example 1:

        Input: arr = [-3, -4, 5], k = 3
        Output: [-4, -3, 5]

    Example 2:

        Input: arr = [4, -4, 4], k = 2
        Output: [4, 4]

    Example 3:

        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [2]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)
    """
def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    Example 1:

        Input: arr = [-3, -4, 5], k = 3
        Output: [-4, -3, 5]

    Example 2:

        Input: arr = [4, -4, 4], k = 2
        Output: [4, 4]

    Example 3:

        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [2]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)
    """
    return sorted(arr, reverse=True)[:k]

def test_maximum():
    assert maximum([-3, -4, 5], 3) == [-4, -3, 5]
    assert maximum([4, -4, 4], 2) == [4, 4]
    assert maximum([-3, 2, 1, 2, -1, -2, 1], 1) == [2]
    assert maximum([1, 2, 3, 4, 5], 0) == []
    assert maximum([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4, 5]
    assert maximum([1, 2, 3, 4, 5], 6) == [1, 2, 3, 4, 5]
    assert maximum([-1, -2, -3, -4, -5], 3) == [-5, -4, -3]
    assert maximum([-1, -2, -3, -4, -5], 0) == []
    assert maximum([-1, -2, -3, -4, -5], 5) == [-5, -4, -3, -2, -1]
    assert maximum([-1, -2, -3, -4, -5], 6) == [-5, -4, -3, -2, -1]
    assert maximum([1, 2, 3, 4, 5], 2) == [4, 5]
    assert maximum([1, 2, 3, 4, 5], 3) == [3, 4, 5]
    assert maximum([1, 2, 3, 4, 5], 4) == [2, 3, 4, 5]
    assert maximum([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4, 5]
    assert maximum([1, 2, 3, 4, 5], 6) == [1, 2, 3, 4, 5]
    assert maximum([-1, -2, -3, -4, -5], 2) == [-4, -3]
    assert maximum([-1, -2, -3, -4, -5], 3) == [-5, -4, -3]
    assert maximum([-1, -2