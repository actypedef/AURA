"""
Write a function to apply a given format string to all of the elements in a list.
assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']
"""
def add_string(nums, string):
    # Apply the format string to each element in the list
    result = [string.format(i) for i in nums]
    return result

# Test the function with the provided test case
assert add_string([1, 2, 3, 4], 'temp{0}') == ['temp1', 'temp2', 'temp3', 'temp4']
