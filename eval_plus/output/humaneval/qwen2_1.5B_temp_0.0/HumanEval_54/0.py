

def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars('abcd', 'dddddddabc')
    True
    >>> same_chars('dddddddabc', 'abcd')
    True
    >>> same_chars('eabcd', 'dddddddabc')
    False
    >>> same_chars('abcd', 'dddddddabce')
    False
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """
def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.
    
    :param s0: First word to compare
    :param s1: Second word to compare
    :return: True if both words contain the same characters, False otherwise
    """
    return set(s0) == set(s1)

# Test cases