"""
Write a function to find the shared elements from the given two lists.
assert set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))) == set((4, 5))
"""
def similar_elements(list1, list2):
    # Convert both lists to sets for easy comparison
    set1 = set(list1)
    set2 = set(list2)
    
    # Find the intersection of the two sets
    shared_elements = set1.intersection(set2)
    
    return shared_elements

# Test the function with provided data points
assert set(similar_elements((3, 4, 5, 6), (5, 7, 4, 10))) == set((4, 5))