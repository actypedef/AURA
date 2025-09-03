"""
Write a function to count the number of sublists containing a particular element.
assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)==3
"""
def count_element_in_list(list1, element):
    # Use a generator expression to count sublists containing the element
    count = sum(1 for sublist in list1 if element in sublist)
    return count

# Test the function with the provided test case
assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 1) == 3