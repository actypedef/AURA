from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    current_group = []
    open_count = 0

    for char in paren_string:
        if char == '(':
            open_count += 1
            current_group.append(char)
        elif char == ')':
            open_count -= 1
            current_group.append(char)

            if open_count == 0:
                result.append(''.join(current_group))
                current_group = []

    return result


def test_separate_paren_groups():
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']
    assert separate_paren_groups('(( )) (( )( )) ( )') == ['(())', '(()())', '()']
    assert separate_paren_groups('') == []
    assert separate_paren_groups('()()()') == ['()', '()', '()']
    assert separate_paren_groups('((()))') == ['((()))']
    assert separate_paren_groups('(()())(())()') == ['(()())', '(())', '()']
    assert separate_paren_groups('()((()))(())') == ['()', '((()))', '(())']
    assert separate_paren_groups('((())())(()())') == ['((())())', '(()())']
    assert separate_paren_groups('(((())))((()))') == ['(((())))', '((()))']
    assert separate_paren_groups('((())())(()())') == ['((())())', '(()())']
    assert separate_paren_groups('((())())(()())') == ['((())())', '(()())']
    assert separate_paren_groups('((())())(()())') == ['((())())', '(()())']
    assert separate_paren_groups('((())())(()())') == ['((())())', '(()())']
    assert separate_paren_groups('((())())(()())') == ['((())())', '(()())']
    assert separate_paren_groups('((())())(()())') == ['((())())', '(()())']
    assert separate_paren_groups('((())())(()())') == ['((())())', '(()())']
    assert separate_paren_groups('((())())(()())') == ['((())())', '(()())']
    assert separate_paren_groups('((())())(()())') == ['((())())', '(()())']
    assert separate_paren_groups('((())())(()())') == ['((())())', '(()())']
    assert separate_paren_groups('((())())(()())') == ['((())())', '(()())']
    assert separate_paren_groups('((())())(()())') == ['((())())', '(()())']
    assert separate_paren_groups('((())())(()())') == ['((())())', '(()())']
    assert separate_paren_groups('((())())(()())') == ['((())())', '(()())']
    assert separate_paren_groups('((())())(()())') == ['((())())', '(()())']
    assert separate_paren_groups('((())())(()())') == ['((())())', '(()())']
    assert separate_paren_groups('((())())