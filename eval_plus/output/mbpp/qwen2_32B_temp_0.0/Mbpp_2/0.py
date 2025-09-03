"""
Write a function to find the shared elements from the given two lists.
assert set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))) == set((4, 5))
"""
def similar_elements(list1, list2):
    """
    This function takes two lists as input and returns a set of elements that are common to both lists.
    """
    # Convert the lists to sets to remove duplicates and make the intersection operation more efficient
    set1 = set(list1)
    set2 = set(list2)
    
    # Use the intersection method to find common elements
    common_elements = set1.intersection(set2)
    
    return common_elements

# Test the function
assert similar_elements((3, 4, 5, 6), (5, 7, 4, 10)) == {4, 5}