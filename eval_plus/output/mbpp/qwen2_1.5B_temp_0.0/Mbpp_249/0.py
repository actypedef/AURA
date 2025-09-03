"""
Write a function to find the intersection of two arrays.
assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9])==[1, 2, 8, 9]
"""
def intersection_array(arr1, arr2):
    # Convert both lists to sets for efficient lookup
    set1 = set(arr1)
    set2 = set(arr2)
    
    # Find the intersection of the two sets
    result = list(set1.intersection(set2))
    
    return result

# Test the function
assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10], [1, 2, 4, 8, 9]) == [1, 2, 8, 9]