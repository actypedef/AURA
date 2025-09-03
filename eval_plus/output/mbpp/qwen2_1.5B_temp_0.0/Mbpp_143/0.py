"""
Write a function to find number of lists present in the given tuple.
assert find_lists(([1, 2, 3, 4], [5, 6, 7, 8])) == 2
"""
def find_lists(tup):
    # Initialize a counter for lists
    list_count = 0
    
    # Iterate through each element in the tuple
    for item in tup:
        # Check if the item is a list
        if isinstance(item, list):
            # Increment the list count
            list_count += 1
            
    # Return the total count of lists
    return list_count

# Test cases to verify the correctness of the function
assert find_lists(([1, 2, 3, 4], [5, 6, 7, 8])) == 2
assert find_lists((['a', 'b'], ['c', 'd', 'e'])) == 2
assert find_lists(([1, 2, 3], [4, 5], [6, 7, 8])) == 3
assert find_lists(('a', 'b', 'c')) == 0