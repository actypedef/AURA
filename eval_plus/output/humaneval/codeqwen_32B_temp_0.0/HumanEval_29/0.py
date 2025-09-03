from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [s for s in strings if s.startswith(prefix)]


def test():
    assert filter_by_prefix([], 'a') == []
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'b') == ['bcd']
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'c') == ['cde']
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'd') == []
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'e') == []
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'f') == []
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'g') == []
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'h') == []
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'i') == []
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'j') == []
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'k') == []
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'l') == []
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'm') == []
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'n') == []
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'o') == []
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'p') == []
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'q') == []
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'r') == []
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 's') == []
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 't') == []
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'u') == []
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'v') == []
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'w') == []
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'x') == []
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'y') == []
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'z') == []
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'A') == []
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'B') == []
    assert filter_by_prefix