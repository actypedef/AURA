

def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    return [x for x in l if x > 0]

def test_get_positive():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
    assert get_positive([-1, -2, -3, -4, -5]) == []
    assert get_positive([0, 0, 0, 0, 0]) == []
    assert get_positive([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert get_positive([-1, -2, 3, -4, 5]) == [3, 5]
    assert get_positive([-1, 2, -4, 5, 6, -7, 8, -9, 10]) == [2, 5, 6, 8, 10]
    assert get_positive([-1, -2, -3, -4, -5, 6, 7, 8, 9, 10]) == [6, 7, 8, 9, 10]
    assert get_positive([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == []
    assert get_positive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert get_positive([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, 11, 12, 13, 14, 15]) == [11, 12, 13, 14, 15]
    assert get_positive([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15]) == []
    assert get_positive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert get_positive([-1, -2, -3, -4,