"""
Write a function to check if all the elements in tuple have same data type or not.
assert check_type((5, 6, 7, 3, 5, 6) ) == True
"""
def check_type(tup):
    # Get the data type of the first element in the tuple
    first_element_type = type(tup[0])
    
    # Check if all elements in the tuple have the same data type as the first element
    for element in tup:
        if type(element) != first_element_type:
            return False
    
    return True

# Test cases
assert check_type((5, 6, 7, 3, 5, 6)) == True
assert check_type((1, "a", 2.5)) == False
assert check_type(("apple", "banana", "cherry")) == True
assert check_type((True, False, True)) == True
assert check_type((1, 2, "three")) == False