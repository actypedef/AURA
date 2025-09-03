"""
Write a function that takes two lists and returns true if they have at least one common element.
assert common_element([1,2,3,4,5], [5,6,7,8,9])==True
"""
def common_element(list1, list2):
    # Iterate through each element in the first list
    for i in range(len(list1)):
        # Check if the current element of list1 exists in list2
        if list1[i] in list2:
            return True  # Return True if a common element is found
    return False  # Return False if no common elements are found

# Test the function with the provided test case
assert common_element([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]) == True
