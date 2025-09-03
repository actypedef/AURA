"""
Write a function that takes two lists and returns true if they have at least one common element.
assert common_element([1,2,3,4,5], [5,6,7,8,9])==True
"""
def common_element(list1, list2):
    # Create sets from both lists to remove duplicates and allow for efficient intersection
    set1 = set(list1)
    set2 = set(list2)
    
    # Check if there is any common element between the two sets
    if set1.intersection(set2):
        return True
    else:
        return False

# Test the function with the provided test case
assert common_element([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]) == True