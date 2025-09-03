"""
Write a function to check whether an element exists within a tuple.
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r')==True
"""
def check_tuplex(tuplex, element):
    # Check if the element exists in the tuple
    return element in tuplex

# Test the function with the provided test case
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'r') == True
