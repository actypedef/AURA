"""
Write a function to sort a given list of strings of numbers numerically. https://www.geeksforgeeks.org/python-sort-numeric-strings-in-a-list/
assert sort_numeric_strings( ['4','12','45','7','0','100','200','-12','-500'])==[-500, -12, 0, 4, 7, 12, 45, 100, 200]
"""
def sort_numeric_strings(lst):
    # Convert all elements in the list to integers for comparison
    lst = [int(x) for x in lst]
    # Sort the list of integers
    lst.sort()
    # Convert the sorted list back to strings
    return [str(x) for x in lst]

# Test the function
assert sort_numeric_strings(['4','12','45','7','0','100','200','-12','-500']) == [-500, -12, 0, 4, 7, 12, 45, 100, 200]