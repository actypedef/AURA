"""
Write a function that takes in a list and element and checks whether all items in the list are equal to the given element.
assert check_element(["green", "orange", "black", "white"],'blue')==False
"""
def check_element(lst, elem):
    return all(item == elem for item in lst)

# Test cases
assert check_element(["green", "orange", "black", "white"], 'blue') == False
assert check_element([10, 20, 30, 40], 10) == True
assert check_element(['apple', 'banana', 'cherry'], 'apple') == True
assert check_element([], 'anything') == True