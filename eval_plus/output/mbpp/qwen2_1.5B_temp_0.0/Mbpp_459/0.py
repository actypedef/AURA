"""
Write a function to remove uppercase substrings from a given string.
assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
"""
def remove_uppercase(s):
    """
    Remove all uppercase substrings from the input string.

    Args:
    s (str): The input string from which uppercase substrings will be removed.

    Returns:
    str: A new string with all uppercase substrings removed.
    """
    return ''.join(c for c in s if not c.isupper())

# Test cases to verify the correctness of the solution
assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
assert remove_uppercase('Python3.8') == 'ython3.8'
assert remove_uppercase('123ABCabcXYZ') == '123bcabxyz'
assert remove_uppercase('UPPERlower') == 'lower'
assert remove_uppercase('') == ''