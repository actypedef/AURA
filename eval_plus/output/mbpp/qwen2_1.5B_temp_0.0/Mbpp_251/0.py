"""
Write a function that takes in a list and an element and inserts the element before each element in the list, and returns the resulting list.
assert insert_element(['Red', 'Green', 'Black'] ,'c')==['c', 'Red', 'c', 'Green', 'c', 'Black']
"""
def insert_element(lst, elem):
    # Initialize an empty list to store the result
    result = []
    # Iterate over each element in the input list
    for item in lst:
        # Append the current element to the result list
        result.append(item)
        # Append the specified element to the result list
        result.append(elem)
    return result

# Test cases to verify the correctness of the function
assert insert_element(['Red', 'Green', 'Black'], 'c') == ['c', 'Red', 'c', 'Green', 'c', 'Black']
assert insert_element([1, 2, 3], 'a') == [a, 1, a, 2, a, 3]
assert insert_element([], 'x') == []