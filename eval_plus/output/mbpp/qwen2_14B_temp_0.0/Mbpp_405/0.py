"""
Write a function to check whether an element exists within a tuple.
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r')==True
"""
def check_tuplex(test_tuplex, value):
    # Check if the value exists in the tuple
    res = value in test_tuplex
    return res

# Test the function with the provided test case
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'r') == True
