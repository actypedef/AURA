
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
    """
    Check if there exists a valid subsequence of brackets where at least one bracket is nested.
    
    :param s: Input string containing only square brackets
    :return: True if there is at least one nested bracket, False otherwise
    """
    stack = []
    for char in s:
        if char == '[':
            stack.append(char)
        elif char == ']':
            if not stack:
                return False
            stack.pop()
            # If stack is not empty after popping, it means there's a nested structure
            if stack:
                return True
    return False

# Test cases to verify the correctness of the function
assert is_nested('[[]]') == True
assert is_nested('[]]]]]]][[[[[]') == False
assert is_nested('[][]') == False
assert is_nested('[]') == False
assert is_nested('[[][]]') == True
assert is_nested('[[]][[') == True