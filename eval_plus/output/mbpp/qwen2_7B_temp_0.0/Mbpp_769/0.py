"""
Write a python function to get the difference between two lists.
assert (Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == [10, 20, 30, 15]
"""
def Diff(list1, list2):
    # Use set comprehension to find elements in list1 that are not in list2
    diff = [x for x in list1 if x not in list2]
    return diff

# Test the function with the provided test case
assert Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]) == [10, 20, 30, 15]
