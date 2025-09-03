"""
Write a python function to check whether a list of numbers contains only one distinct element or not.
assert unique_Element([1,1,1]) == True
"""
def unique_Element(lst):
    return len(set(lst)) == 1

# Test cases
assert unique_Element([1,1,1]) == True
assert unique_Element([2,3,4]) == False
assert unique_Element([]) == True
assert unique_Element([5]) == True
assert unique_Element([1,2,3,4,5]) == True
assert unique_Element([1,2,3,4,5,6]) == False