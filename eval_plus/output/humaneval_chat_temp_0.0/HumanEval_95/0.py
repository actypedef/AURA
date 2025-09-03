
def check_dict_case(dict):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    Examples:
    check_dict_case({"a":"apple", "b":"banana"}) should return True.
    check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) should return False.
    check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) should return False.
    check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) should return False.
    check_dict_case({"STATE":"NC", "ZIP":"12345" }) should return True.
    """
def check_dict_case(dictionary):
    """
    Check if all keys in the dictionary are either all lowercase or all uppercase strings.
    Return False if the dictionary is empty or if it contains non-string keys.
    
    Args:
    dictionary (dict): The dictionary to check.

    Returns:
    bool: True if all keys are strings in the same case (all lowercase or all uppercase), False otherwise.
    """

    # Early return for empty dictionary
    if not dictionary:
        return False

    has_lower = has_upper = False

    for key in dictionary.keys():
        # Check if the key is a string
        if not isinstance(key, str):
            return False
        
        # Update flags based on the case of the current key
        if key.islower():
            has_lower = True
        elif key.isupper():
            has_upper = True
        else:
            # If the key is neither all lower nor all upper, return False
            return False
        
        # If both flags are True, it means we have seen both cases, so return False
        if has_lower and has_upper:
            return False

    return True

# Test cases