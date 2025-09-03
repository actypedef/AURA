"""
Write a function that takes in a list and an integer n and returns a list containing the n largest items from the list.
assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([100,90])
"""
def larg_nnum(lst, n):
    # Sort the list in descending order
    lst.sort(reverse=True)
    # Return the first n elements of the sorted list
    return lst[:n]

# Test the function
assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2)) == set([100,90])