"""
Write a function to flatten a given nested list structure.
assert flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]])==[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
"""
def flatten_list(nested_list):
    # Initialize an empty list to store the flattened elements
    flat_list = []
    
    # Iterate through each element in the nested list
    for item in nested_list:
        # Check if the current item is a list
        if isinstance(item, list):
            # Extend the flat_list with the flattened version of the current item
            flat_list.extend(flatten_list(item))
        else:
            # Append the non-list item directly to the flat_list
            flat_list.append(item)
    
    # Return the fully flattened list
    return flat_list

# Test the function with the provided test case
assert flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]) == [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]