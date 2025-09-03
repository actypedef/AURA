"""
Write a function to remove consecutive duplicates of a given list.
assert consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
"""
def consecutive_duplicates(nums):
    # Initialize an empty list to store unique elements
    result = []
    
    # Iterate through each element in the input list
    for i in range(len(nums)):
        # Check if it's the first element or not equal to the previous element
        if i == 0 or nums[i] != nums[i - 1]:
            # If so, append it to the result list
            result.append(nums[i])
    
    return result

# Test the function with the provided test case
assert consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
