
def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    '''
def is_nested(s: str) -> bool:
    stack = []
    for char in s:
        if char == '[':
            stack.append(char)
        elif char == ']' and stack:
            stack.pop()
        else:
            return False
    return len(stack) > 1

# Test cases