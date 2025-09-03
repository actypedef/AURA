"""
Write a python function to find the length of the smallest list in a list of lists.
assert Find_Min_Length([[1],[1,2]]) == 1
"""
def Find_Min_Length(list1):
    # Find the minimum length among all sublists in the list of lists
    min_length = min(len(x) for x in list1)
    return min_length

# Test the function with the provided test case
assert Find_Min_Length([[1], [1, 2]]) == 1
