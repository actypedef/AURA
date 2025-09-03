"""
Write a function to check if a dictionary is empty
assert my_dict({10})==False
"""
def is_empty(dictionary):
    """
    Check if a dictionary is empty

    Args:
    dictionary (dict): The dictionary to check

    Returns:
    bool: True if the dictionary is empty, False otherwise
    """
    return not dictionary

# Test cases
assert is_empty({10}) == False
assert is_empty({}) == True
assert is_empty({'a': 1, 'b': 2}) == False
assert is_empty({'a': None, 'b': None}) == True
assert is_empty({'a': 1, 'b': 2, 'c': 3}) == False