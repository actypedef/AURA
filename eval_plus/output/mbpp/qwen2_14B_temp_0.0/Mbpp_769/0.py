"""
Write a python function to get the difference between two lists.
assert (Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == [10, 20, 30, 15]
"""
def Diff(li1, li2):
    # Use list comprehension to find elements in li1 that are not in li2
    result = [i for i in li1 if i not in li2]
    return result

# Test the function with the provided test case
assert (Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == [10, 20, 30, 15]
