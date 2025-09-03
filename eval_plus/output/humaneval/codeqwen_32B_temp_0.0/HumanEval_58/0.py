

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    return sorted(set(l1).intersection(set(l2)))

def test_common():
    assert common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]) == [1, 5, 653]
    assert common([5, 3, 2, 8], [3, 2]) == [2, 3]
    assert common([1, 2, 3], [4, 5, 6]) == []
    assert common([1, 2, 3], [1, 2, 3]) == [1, 2, 3]
    assert common([1, 2, 3], [3, 2, 1]) == [1, 2, 3]
    assert common([1, 2, 3], [1, 2, 3, 4, 5]) == [1, 2, 3]
    assert common([1, 2, 3, 4, 5], [1, 2, 3]) == [1, 2, 3]
    assert common([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert common([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]) == []
    assert common([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert common([1, 2, 3, 4, 5], [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5]
    assert common([1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert common([1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 11, 12, 13, 14, 15]) == [1, 2, 3, 4, 5]
    assert common([1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 