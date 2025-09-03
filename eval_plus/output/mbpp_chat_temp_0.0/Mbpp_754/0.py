"""
We say that an element is common for lists l1, l2, l3 if it appears in all three lists under the same index. Write a function to find common elements from three lists. The function should return a list.
assert extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7])==[1, 7]
"""
def extract_index_list(l1, l2, l3):
    # Use zip to iterate over the three lists simultaneously
    # Filter to include only those elements where all three values are equal
    result = [x for x, y, z in zip(l1, l2, l3) if x == y == z]
    return result

# Test the function with the provided test case
assert extract_index_list([1, 1, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 7], [0, 1, 2, 3, 4, 5, 7]) == [1, 7]