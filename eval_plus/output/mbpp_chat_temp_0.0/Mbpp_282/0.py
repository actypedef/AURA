"""
Write a function to subtract two lists element-wise.
assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]
"""
def sub_list(list1, list2):
    # Use list comprehension to iterate through both lists simultaneously
    # Subtract each pair of elements from the two lists
    result = [i - j for i, j in zip(list1, list2)]
    return result

# Test the function with the provided test case
assert sub_list([1, 2, 3], [4, 5, 6]) == [-3, -3, -3]
