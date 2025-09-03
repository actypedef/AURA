"""
Write a function to remove consecutive duplicates of a given list.
assert consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
"""
def consecutive_duplicates(nums):
    # Initialize an empty list to store the result
    res = []
    
    # Iterate through the input list
    for i in range(len(nums)):
        # Check if the current element is not equal to the previous one (if it's the first element or different)
        if i == 0 or nums[i] != nums[i - 1]:
            # Append the element to the result list
            res.append(nums[i])
    
    # Return the result list
    return res

# Test the function with the provided test case
assert consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]