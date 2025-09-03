"""
The input is defined as two lists of the same length. Write a function to count indices where the lists have the same values.
assert count_same_pair([1, 2, 3, 4, 5, 6, 7, 8],[2, 2, 3, 1, 2, 6, 7, 9])==4
"""
def count_same_pair(list1, list2):
    # Initialize a counter for matching pairs
    match = 0
    
    # Iterate over each pair of elements from both lists
    for i in range(len(list1)):
        # Check if the current elements from both lists are equal
        if list1[i] == list2[i]:
            # Increment the counter if they match
            match += 1
            
    # Return the total number of matching pairs
    return match

# Test the function with the provided test case
assert count_same_pair([1, 2, 3, 4, 5, 6, 7, 8], [2, 2, 3, 1, 2, 6, 7, 9]) == 4