"""
Write a function to flatten a list and sum all of its elements.
assert recursive_list_sum(([1, 2, [3,4],[5,6]]))==21
"""
def recursive_list_sum(lst):
    # Initialize sum to zero
    total = 0
    
    # Iterate through each element in the list
    for i in lst:
        # Check if the element is a list
        if isinstance(i, list):
            # Recursively call the function if it's a list
            total += recursive_list_sum(i)
        else:
            # Add the element to the total sum if it's not a list
            total += i
    
    # Return the total sum of the list elements
    return total

# Test the function with the provided test case
assert recursive_list_sum([1, 2, [3, 4], [5, 6]]) == 21