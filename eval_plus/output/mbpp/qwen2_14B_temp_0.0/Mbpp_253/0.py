"""
Write a python function that returns the number of integer elements in a given list.
assert count_integer([1,2,'abc',1.2]) == 2
"""
def count_integer(lst):
    # Initialize a counter for integer elements
    count = 0
    
    # Iterate through each element in the list
    for i in lst:
        # Check if the element is an integer
        if type(i) == int:
            # Increment the counter if it is an integer
            count += 1
    
    # Return the total count of integer elements
    return count

# Test the function with the provided test case
assert count_integer([1, 2, 'abc', 1.2]) == 2
