"""
Write a function that takes in a list and an element and inserts the element before each element in the list, and returns the resulting list.
assert insert_element(['Red', 'Green', 'Black'] ,'c')==['c', 'Red', 'c', 'Green', 'c', 'Black']
"""
def insert_element(lst, element):
    # Initialize an empty list to store the result
    res = []
    
    # Iterate over each item in the original list
    for i in lst:
        # Append the given element followed by the current item to the result list
        res.extend([element, i])
    
    return res

# Test the function with the provided test case
assert insert_element(['Red', 'Green', 'Black'], 'c') == ['c', 'Red', 'c', 'Green', 'c', 'Black']
