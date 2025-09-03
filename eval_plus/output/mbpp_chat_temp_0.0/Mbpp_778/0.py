"""
Write a function to pack consecutive duplicates of a given list elements into sublists.
assert pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])==[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
"""
def pack_consecutive_duplicates(nums):
    # Initialize an empty list to store the result
    res = []
    
    # Iterate over the input list using enumerate to get both index and value
    for i, num in enumerate(nums):
        # Check if it's the first element or not equal to the previous one
        if i == 0 or nums[i - 1] != num:
            # If so, start a new sublist with the current number
            res.append([num])
        else:
            # Otherwise, append the current number to the last sublist
            res[-1].append(num)
    
    return res

# Test the function with the provided test case
assert pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]) == [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]