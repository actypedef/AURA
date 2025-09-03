"""
Write a function to find the maximum value in a given heterogeneous list.
assert max_val(['Python', 3, 2, 4, 5, 'version'])==5
"""
def max_val(lst):
    # Initialize a variable to store the maximum integer found
    max_int = -1
    
    # Iterate through each element in the list
    for i in lst:
        # Check if the current element is an integer and greater than the current max_int
        if isinstance(i, int) and i > max_int:
            # Update max_int with the new maximum integer
            max_int = i
            
    return max_int

# Test the function with the provided test case
assert max_val(['Python', 3, 2, 4, 5, 'version']) == 5