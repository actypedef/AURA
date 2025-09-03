"""
The input is defined as two lists of the same length. Write a function to count indices where the lists have the same values.
assert count_same_pair([1, 2, 3, 4, 5, 6, 7, 8],[2, 2, 3, 1, 2, 6, 7, 9])==4
"""
def count_same_pair(nums1, nums2):
    # Initialize a counter for matching pairs
    count = 0
    
    # Iterate through each pair of elements from both lists
    for i in range(len(nums1)):
        if nums1[i] == nums2[i]:
            count += 1
            
    return count

# Test the function with the provided test case
assert count_same_pair([1, 2, 3, 4, 5, 6, 7, 8], [2, 2, 3, 1, 2, 6, 7, 9]) == 4