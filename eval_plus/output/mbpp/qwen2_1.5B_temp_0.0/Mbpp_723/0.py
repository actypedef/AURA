"""
The input is defined as two lists of the same length. Write a function to count indices where the lists have the same values.
assert count_same_pair([1, 2, 3, 4, 5, 6, 7, 8],[2, 2, 3, 1, 2, 6, 7, 9])==4
"""
def count_same_pair(list1, list2):
    # Initialize a counter for matching pairs
    match_count = 0
    
    # Iterate through both lists simultaneously
    for i in range(len(list1)):
        # Check if the elements at the current index are equal
        if list1[i] == list2[i]:
            # Increment the counter if they are equal
            match_count += 1
            
    # Return the total count of matching pairs
    return match_count

# Test the function with the provided data points
assert count_same_pair([1, 2, 3, 4, 5, 6, 7, 8], [2, 2, 3, 1, 2, 6, 7, 9]) == 4