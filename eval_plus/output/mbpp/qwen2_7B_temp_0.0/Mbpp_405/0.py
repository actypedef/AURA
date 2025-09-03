"""
Write a function to check whether an element exists within a tuple.
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r')==True
"""
def check_tuplex(test_tuplex, ele):
    # Check if the element exists in the tuple
    return ele in test_tuplex

# Test the function with the provided data point
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'r') == True
