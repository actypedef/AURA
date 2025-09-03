"""
Write a python function to count true booleans in the given list.
assert count([True,False,True]) == 2
"""
def count(lst):
    # Initialize a counter for True values
    count = 0
    
    # Iterate through each element in the list
    for i in lst:
        # Check if the element is True
        if i == True:
            # Increment the counter if the element is True
            count += 1
    
    # Return the total count of True values
    return count

# Test the function with the provided test case
assert count([True, False, True]) == 2
