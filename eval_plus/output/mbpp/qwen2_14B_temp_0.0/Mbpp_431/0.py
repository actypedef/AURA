"""
Write a function that takes two lists and returns true if they have at least one common element.
assert common_element([1,2,3,4,5], [5,6,7,8,9])==True
"""
def common_element(list1, list2):
    # Convert the first list to a set for fast lookup
    set1 = set(list1)
    
    # Iterate through each element in the second list
    for element in list2:
        # Check if the element is in the set created from the first list
        if element in set1:
            return True
    
    # Return False if no common elements are found
    return False

# Test the function with the provided test case
assert common_element([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]) == True
