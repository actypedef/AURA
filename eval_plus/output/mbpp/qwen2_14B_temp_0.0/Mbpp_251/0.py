"""
Write a function that takes in a list and an element and inserts the element before each element in the list, and returns the resulting list.
assert insert_element(['Red', 'Green', 'Black'] ,'c')==['c', 'Red', 'c', 'Green', 'c', 'Black']
"""
def insert_element(lst, element):
    # Create a new list by iterating over each item in the original list
    result = [value for item in lst for value in (element, item)]
    return result

# Test the function with the provided test case
assert insert_element(['Red', 'Green', 'Black'], 'c') == ['c', 'Red', 'c', 'Green', 'c', 'Black']
