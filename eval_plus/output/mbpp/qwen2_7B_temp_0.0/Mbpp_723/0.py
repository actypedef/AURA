"""
The input is defined as two lists of the same length. Write a function to count indices where the lists have the same values.
assert count_same_pair([1, 2, 3, 4, 5, 6, 7, 8],[2, 2, 3, 1, 2, 6, 7, 9])==4
"""
def count_same_pair(list1, list2):
    # Initialize a counter for matching pairs
    match_count = 0
    
    # Iterate over the elements of both lists simultaneously using zip
    for item1, item2 in zip(list1, list2):
        # Check if the current items from both lists are equal
        if item1 == item2:
            # Increment the counter if they match
            match_count += 1
    
    # Return the total count of matching pairs
    return match_count

# Test the function with the provided test case
assert count_same_pair([1, 2, 3, 4, 5, 6, 7, 8], [2, 2, 3, 1, 2, 6, 7, 9]) == 4