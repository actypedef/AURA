"""
Write a python function to check whether the given list contains consecutive numbers or not.
assert check_Consecutive([1,2,3,4,5]) == True
"""
def check_Consecutive(lst):
    # Sort the list to ensure the numbers are in ascending order
    lst.sort()
    
    # Check if each element is equal to its previous element plus one
    for i in range(len(lst) - 1):
        if lst[i] + 1 != lst[i + 1]:
            return False
    return True

# Test the function with the provided test case
assert check_Consecutive([1, 2, 3, 4, 5]) == True
