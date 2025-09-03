"""
Write a python function to get the difference between two lists.
assert (Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == [10, 20, 30, 15]
"""
def Diff(list1, list2):
    # Use set operations to find elements in list1 that are not in list2
    return list(set(list1) - set(list2))

# Test the function with the provided test case
assert (Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == [10, 20, 30, 15]
