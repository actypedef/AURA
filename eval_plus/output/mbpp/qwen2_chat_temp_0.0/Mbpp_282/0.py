"""
Write a function to subtract two lists element-wise.
assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]
"""
def sub_list(list1, list2):
    # Use zip to iterate over both lists simultaneously and subtract elements
    result = [x - y for x, y in zip(list1, list2)]
    return result

# Test the function with the provided test case
assert sub_list([1, 2, 3], [4, 5, 6]) == [-3, -3, -3]
