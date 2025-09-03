"""
Write a function to apply a given format string to all of the elements in a list.
assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']
"""
def add_string(lst, fmt):
    # Use list comprehension to apply the format string to each element in the list
    return [fmt.format(i) for i in lst]

# Test the function with the provided test case
assert add_string([1, 2, 3, 4], 'temp{0}') == ['temp1', 'temp2', 'temp3', 'temp4']
