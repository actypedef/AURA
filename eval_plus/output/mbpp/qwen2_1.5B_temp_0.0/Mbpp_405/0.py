"""
Write a function to check whether an element exists within a tuple.
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r')==True
"""
def check_tuplex(tuplex, element):
    """
    Check if an element exists within a tuple.

    Args:
    tuplex (tuple): The tuple to search within.
    element: The element to search for.

    Returns:
    bool: True if the element exists in the tuple, False otherwise.
    """
    return element in tuplex

# Test cases
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'r') == True
assert check_tuplex(('a', 'b', 'c'), 'd') == False
assert check_tuplex((10, 20, 30), 25) == False
assert check_tuplex(('x', 'y', 'z'), 'x') == True
assert check_tuplex(('apple', 'banana', 'cherry'), 'date') == False