"""
Write a function to locate the left insertion point for a specified value in sorted order. https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-24.php
assert left_insertion([1,2,4,5],6)==4
"""
def left_insertion(arr, x):
    # Initialize the index to 0
    i = 0
    # Iterate through the array until we find the correct position
    while i < len(arr) and arr[i] < x:
        i += 1
    # Return the index where the element should be inserted
    return i

# Test the function with the provided test case
assert left_insertion([1,2,4,5],6)==4