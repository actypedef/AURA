"""
Write a function that takes in a list and an integer n and returns a list containing the n largest items from the list.
assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([100,90])
"""
def larg_nnum(list1, n):
    # Sort the list in ascending order
    list1.sort()
    # Return the last n elements from the sorted list
    return list1[-n:]

# Test the function with the provided test case
assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 2)) == set([100, 90])
