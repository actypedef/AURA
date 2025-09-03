"""
Write a function to locate the left insertion point for a specified value in sorted order. https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-24.php
assert left_insertion([1,2,4,5],6)==4
"""
def left_insertion(a, x):
    # Initialize the start index
    low = 0
    
    # Iterate through the list to find the correct insertion point
    for i in range(len(a)):
        # Check if the current element is greater than or equal to x
        if a[i] >= x:
            # Return the current index if the condition is met
            return i
    
    # Return the length of the list if no suitable position is found
    return len(a)

# Test the function with the provided test case
assert left_insertion([1, 2, 4, 5], 6) == 4
