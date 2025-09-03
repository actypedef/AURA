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
    """Filter given list of any python values only for integers
    
    Args:
        values (List[Any]): A list containing elements of any type.
    
    Returns:
        List[int]: A list containing only integer elements from the input list.
    
    Examples:
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]

# Test cases to verify the correctness of the function