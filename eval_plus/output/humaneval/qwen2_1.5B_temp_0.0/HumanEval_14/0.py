from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
# Importing necessary library
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i] for i in range(1, len(string)+1)]

# Test cases to verify the correctness of the function
assert all_prefixes('abc') == ['a', 'ab', 'abc'], "Test case 1 failed"
assert all_prefixes('hello') == ['h', 'he', 'hel', 'hell', 'hello'], "Test case 2 failed"
assert all_prefixes('') == [], "Test case 3 failed"