"""
Write a function to rotate a given list by specified number of items to the right direction. https://www.geeksforgeeks.org/python-program-right-rotate-list-n/
assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3)==[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
"""
def rotate_right(lst, n):
    # Calculate the effective rotation needed
    n = n % len(lst)
    
    # Perform the rotation
    rotated_lst = lst[-n:] + lst[:-n]
    
    return rotated_lst

# Test cases
assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3) == [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
assert rotate_right(['a', 'b', 'c', 'd'], 2) == ['c', 'd', 'a', 'b']
assert rotate_right([], 5) == []
assert rotate_right([1], 10) == [1]