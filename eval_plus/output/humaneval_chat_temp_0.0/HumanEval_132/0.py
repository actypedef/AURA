
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
    # Initialize counters for open and close brackets
    open_brackets = 0
    nested = False
    
    # Iterate through each character in the string
    for char in s:
        if char == '[':
            open_brackets += 1
            # If there's more than one open bracket before this one, it's nested
            if open_brackets > 1:
                nested = True
        elif char == ']':
            open_brackets -= 1
            # If we have too many closing brackets, return False immediately
            if open_brackets < 0:
                return False
    
    # Return True if there was at least one nested pair and all brackets are closed
    return nested and open_brackets == 0

# Test cases to verify the correctness of the function