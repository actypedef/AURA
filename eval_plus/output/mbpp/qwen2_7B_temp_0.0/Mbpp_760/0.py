"""
Write a python function to check whether a list of numbers contains only one distinct element or not.
assert unique_Element([1,1,1]) == True
"""
def unique_Element(nums):
    # Check if all elements in the list are equal
    return len(set(nums)) == 1

# Test the function with the provided test case
assert unique_Element([1, 1, 1]) == True
