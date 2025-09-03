"""
Write a function to divide two lists element wise.
assert div_list([4,5,6],[1, 2, 3])==[4.0,2.5,2.0]
"""
def div_list(list1, list2):
    # Use list comprehension to iterate over both lists simultaneously
    return [i / j for i, j in zip(list1, list2)]

# Test the function with the provided test case
assert div_list([4, 5, 6], [1, 2, 3]) == [4.0, 2.5, 2.0]
