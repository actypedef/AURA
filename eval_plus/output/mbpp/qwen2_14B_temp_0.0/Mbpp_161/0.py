"""
Write a function to remove all elements from a given list present in another list.
assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]) == [1, 3, 5, 7, 9, 10]
"""
def remove_elements(list1, list2):
    # Use a list comprehension to filter out elements of list1 that are present in list2
    result = [i for i in list1 if i not in list2]
    return result

# Test the function with the provided test case
assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]) == [1, 3, 5, 7, 9, 10]
