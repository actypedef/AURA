from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]


def test_filter_integers():
    assert filter_integers(['a', 3.14, 5]) == [5]
    assert filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3]
    assert filter_integers([1, 2, 3, 'abc', {}, [], 4.5, 6]) == [1, 2, 3, 6]
    assert filter_integers([1, 2, 3, 'abc', {}, [], 4.5, 6, 'def']) == [1, 2, 3, 6]
    assert filter_integers([1, 2, 3, 'abc', {}, [], 4.5, 6, 'def', 7]) == [1, 2, 3, 6, 7]
    assert filter_integers([1, 2, 3, 'abc', {}, [], 4.5, 6, 'def', 7, 8]) == [1, 2, 3, 6, 7, 8]
    assert filter_integers([1, 2, 3, 'abc', {}, [], 4.5, 6, 'def', 7, 8, 9]) == [1, 2, 3, 6, 7, 8, 9]
    assert filter_integers([1, 2, 3, 'abc', {}, [], 4.5, 6, 'def', 7, 8, 9, 10]) == [1, 2, 3, 6, 7, 8, 9, 10]
    assert filter_integers([1, 2, 3, 'abc', {}, [], 4.5, 6, 'def', 7, 8, 9, 10, 11]) == [1, 2, 3, 6, 7, 8, 9, 10, 11]
    assert filter_integers([1, 2, 3, 'abc', {}, [], 4.5, 6, 'def', 7, 8, 9, 10, 11, 12]) == [1, 2, 3, 6, 7, 8, 9, 10, 11, 12]
    assert filter_integers([1, 2, 3, 'abc', {}, [], 4.5, 6, 'def', 7, 8, 9, 10, 11, 12, 13]) == [1, 2, 3, 6, 7, 8, 9, 10, 11, 12, 13]
    assert filter_integers([1, 2, 3, 'abc', {}, [], 4.5, 6, 'def', 7, 8, 9