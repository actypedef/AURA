"""
Write a function to toggle the case of all characters in a string.
assert toggle_string("Python")==("pYTHON")
"""
def toggle_string(s):
    """
    Toggle the case of all characters in a string.
    
    Args:
    s (str): The input string whose characters' cases will be toggled.
    
    Returns:
    str: A new string with each character's case toggled from uppercase to lowercase or vice versa.
    """
    return ''.join([char.lower() if char.isupper() else char.upper() for char in s])

# Test the function
assert toggle_string("Python") == "pYTHON"
