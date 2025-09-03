"""
Write a function to count the number of sublists containing a particular element.
assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)==3
"""
def count_element_in_list(lst, element):
    # Initialize a counter for the occurrences of the element
    count = 0
    
    # Iterate through each sublist in the list
    for sublist in lst:
        # Check if the element is present in the current sublist
        if element in sublist:
            # Increment the counter if the element is found
            count += 1
            
    # Return the total count of occurrences
    return count

# Test the function with the provided test case
assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1) == 3