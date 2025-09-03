"""
Write a function that takes in a list and element and checks whether all items in the list are equal to the given element.
assert check_element(["green", "orange", "black", "white"],'blue')==False
"""
def check_element(lst, element):
    # Check if all elements in the list are equal to the given element
    return all(item == element for item in lst)

# Test the function with the provided test case
assert check_element(["green", "orange", "black", "white"], 'blue') == False
