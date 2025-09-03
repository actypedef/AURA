"""
Write a function to count number items that are identical in the same position of three given lists.
assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9])==3
"""
def count_samepair(list1, list2, list3):
    # Initialize a counter for matching elements
    match_count = 0
    
    # Iterate through each element in the lists
    for i in range(len(list1)):
        # Check if the current element is the same in all three lists at the same index
        if list1[i] == list2[i] == list3[i]:
            # Increment the counter if the condition is met
            match_count += 1
            
    # Return the total count of matching elements
    return match_count

# Test the function with provided data points
assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9])==3