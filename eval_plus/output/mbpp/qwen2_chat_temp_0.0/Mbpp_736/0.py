"""
Write a function to locate the left insertion point for a specified value in sorted order. https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-24.php
assert left_insertion([1,2,4,5],6)==4
"""
def left_insertion(arr, x):
    # Initialize the start index to 0
    start = 0
    
    # Iterate through each element in the array
    for i in range(len(arr)):
        # Check if the current element is greater than or equal to x
        if arr[i] >= x:
            # Return the current index as the left insertion point
            return i
    
    # If no element is found that is greater than or equal to x, return the length of the array
    return len(arr)

# Test the function with the provided test case
assert left_insertion([1, 2, 4, 5], 6) == 4