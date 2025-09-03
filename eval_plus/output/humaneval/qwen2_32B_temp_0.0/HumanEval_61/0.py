

def correct_bracketing(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """
def correct_bracketing(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """
    stack = []
    for char in brackets:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return not stack


def test_correct_bracketing():
    assert correct_bracketing("(") == False
    assert correct_bracketing("()") == True
    assert correct_bracketing("(()())") == True
    assert correct_bracketing(")(()") == False
    assert correct_bracketing("(()(()))") == True
    assert correct_bracketing("(()(())))") == False
    assert correct_bracketing("(()(()))(") == False
    assert correct_bracketing("(()(()))()") == True
    assert correct_bracketing("(()(()))()(") == False
    assert correct_bracketing("(()(()))()()") == True
    assert correct_bracketing("(()(()))()()(") == False
    assert correct_bracketing("(()(()))()()()") == True
    assert correct_bracketing("(()(()))()()()(") == False
    assert correct_bracketing("(()(()))()()()()") == True
    assert correct_bracketing("(()(()))()()()()(") == False
    assert correct_bracketing("(()(()))()()()()()") == True
    assert correct_bracketing("(()(()))()()()()()(") == False
    assert correct_bracketing("(()(()))()()()()()()") == True
    assert correct_bracketing("(()(()))()()()()()()(") == False
    assert correct_bracketing("(()(()))()()()()()()()") == True
    assert correct_bracketing("(()(()))()()()()()()()(") == False
    assert correct_bracketing("(()(()))()()()()()()()()") == True
    assert correct_bracketing("(()(()))()()()()()()()()(") == False
    assert correct_bracketing("(()(()))()()()()()()()()()") == True
    assert correct_bracketing("(()(()))()()()()()()()()()(") == False
    assert correct_bracketing("(()(()))()()()()()()()()()()") == True
    assert correct_bracketing("(()(()))()()()()()()()()()()(") == False
    assert correct_bracketing("(()(()))()()()()()()()()()()()") == True
    assert correct_bracketing("(()(()))()()()()()()()()()()()(") == False
    assert correct_bracketing("(()(()))()()()()()()()()()()()()") == True
    assert correct_bracketing("(()(()))()()()()()()()()()()()()(") == False
    assert correct_bracketing("(()(()))()()()()()()()()()()()()()") == True
    assert correct_bracketing("(()(()))