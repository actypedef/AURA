"""
Write a function to pack consecutive duplicates of a given list elements into sublists.
assert pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])==[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
"""
def pack_consecutive_duplicates(nums):
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over the list using enumerate to get both index and value
    for i, num in enumerate(nums):
        # Check if it's the first element or not equal to the previous element
        if i == 0 or nums[i] != nums[i - 1]:
            # If so, start a new sublist
            result.append([])
        
        # Append the current number to the last sublist in the result
        result[-1].append(num)
    
    return result

# Test the function with the provided test case
assert pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]) == [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
