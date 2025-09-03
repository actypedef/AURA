"""
Write a function to count number items that are identical in the same position of three given lists.
assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9])==3
"""
def count_samepair(list1, list2, list3):
    # Initialize a counter for matching elements at the same index
    match = 0
    
    # Iterate through each element in the lists using zip to handle multiple lists simultaneously
    for i, j, k in zip(list1, list2, list3):
        # Check if all elements at the current index are equal
        if i == j == k:
            # Increment the counter if they are equal
            match += 1
    
    # Return the total count of matching elements
    return match

# Test the function with the provided test case
assert count_samepair([1, 2, 3, 4, 5, 6, 7, 8], [2, 2, 3, 1, 2, 6, 7, 9], [2, 1, 3, 1, 2, 6, 7, 9]) == 3