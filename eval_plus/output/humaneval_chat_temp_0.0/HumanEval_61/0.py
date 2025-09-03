

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
        if char == '(':
            # Increment the counter for an open bracket
            open_brackets += 1
        elif char == ')':
            # Decrement the counter for a close bracket
            open_brackets -= 1
        
        # If at any point the number of close brackets exceeds open ones, return False
        if open_brackets < 0:
            return False
    
    # If the loop completes and all open brackets have been closed, return True
    return open_brackets == 0

# Test cases to verify the correctness of the function