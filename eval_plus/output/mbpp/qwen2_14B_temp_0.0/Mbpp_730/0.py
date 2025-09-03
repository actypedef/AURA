"""
Write a function to remove consecutive duplicates of a given list.
assert consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
"""
def consecutive_duplicates(nums):
    # Initialize an empty list to store the result
    result = []
    
    # Iterate through the input list
    for i in range(len(nums)):
        # Add the element to the result if it's the first occurrence or different from the last added element
        if i == 0 or nums[i] != nums[i - 1]:
            result.append(nums[i])
    
    return result

# Test the function with the provided test case
assert consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
