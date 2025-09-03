"""
Write a function that takes in a list and an integer n and returns a list containing the n largest items from the list.
assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([100,90])
"""
def larg_nnum(nums, n):
    # Sort the list in ascending order
    nums.sort()
    # Return the last n elements of the sorted list as a new list
    return nums[-n:]

# Test the function with the provided test case
assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 2)) == set([100, 90])
