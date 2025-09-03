"""
Write a function to sort a given list of strings of numbers numerically. https://www.geeksforgeeks.org/python-sort-numeric-strings-in-a-list/
assert sort_numeric_strings( ['4','12','45','7','0','100','200','-12','-500'])==[-500, -12, 0, 4, 7, 12, 45, 100, 200]
"""
def sort_numeric_strings(nums_str):
    # Convert each string in the list to an integer
    result = [int(x) for x in nums_str]
    # Sort the list of integers
    result.sort()
    return result

# Test the function with the provided test case
assert sort_numeric_strings(['4', '12', '45', '7', '0', '100', '200', '-12', '-500']) == [-500, -12, 0, 4, 7, 12, 45, 100, 200]
