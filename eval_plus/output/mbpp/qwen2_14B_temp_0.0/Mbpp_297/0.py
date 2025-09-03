"""
Write a function to flatten a given nested list structure.
assert flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]])==[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
"""
def flatten_list(nested_list):
    # Initialize an empty list to store the flattened elements
    flat_list = []
    
    # Iterate through each element in the nested list
    for element in nested_list:
        # If the element is a list, extend the flat_list with its contents
        if isinstance(element, list):
            flat_list.extend(flatten_list(element))
        else:
            # If the element is not a list, append it to the flat_list
            flat_list.append(element)
    
    return flat_list

# Test the function with the provided test case
assert flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]) == [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
