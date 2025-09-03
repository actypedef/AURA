

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
def correct_bracketing(brackets: str) -> bool:
    # Initialize a counter for open brackets
    open_brackets = 0
    
    # Iterate through each character in the input string
    for char in brackets:
        # If an open bracket is found, increment the counter
        if char == '(':
            open_brackets += 1
        # If a close bracket is found, decrement the counter
        elif char == ')':
            open_brackets -= 1
        
        # If at any point the number of open brackets becomes negative, return False
        if open_brackets < 0:
            return False
    
    # If the loop completes and all brackets are balanced, return True
    return open_brackets == 0

# Test cases to verify the correctness of the function
assert correct_bracketing("(") == False
assert correct_bracketing("()") == True
assert correct_bracketing("(()())") == True
assert correct_bracketing(")(()") == False