"""
Write a function to rotate a given list by specified number of items to the right direction. https://www.geeksforgeeks.org/python-program-right-rotate-list-n/
assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3)==[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
"""
def rotate_right(arr, n):
    # Calculate the effective rotation needed
    n = n % len(arr)
    
    # Split the array into two parts
    first_part = arr[-n:]
    second_part = arr[:-n]
    
    # Concatenate the two parts to get the rotated array
    return first_part + second_part

# Test the function with the provided test case
assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3) == [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]