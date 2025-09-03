"""
Write a function to count the number of sublists containing a particular element.
assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)==3
"""
def count_element_in_list(lst, x):
    # Initialize a counter to keep track of sublists containing the element x
    count = 0
    
    # Iterate through each sublist in the list
    for sublist in lst:
        # Check if the element x is in the current sublist
        if x in sublist:
            # If found, increment the counter
            count += 1
            
    # Return the total count of sublists containing the element x
    return count

# Test the function with the provided test case
assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 1) == 3