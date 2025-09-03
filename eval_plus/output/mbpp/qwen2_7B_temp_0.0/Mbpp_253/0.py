"""
Write a python function that returns the number of integer elements in a given list.
assert count_integer([1,2,'abc',1.2]) == 2
"""
def count_integer(lst):
    # Initialize a counter for integers
    count = 0
    
    # Iterate through each element in the list
    for i in lst:
        # Check if the element is an instance of int
        if isinstance(i, int):
            count += 1
    
    # Return the total count of integer elements
    return count

# Test the function with the provided test case
assert count_integer([1, 2, 'abc', 1.2]) == 2
