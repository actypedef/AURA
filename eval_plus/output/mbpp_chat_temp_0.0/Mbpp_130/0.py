"""
Write a function to find the item with maximum frequency in a given list.
assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])==2
"""
def max_occurrences(nums):
    # Initialize variables to store the current maximum count and the number with this count
    max_count = 0
    max_num = None
    
    # Iterate through each unique number in the list
    for num in set(nums):
        # Count occurrences of the current number in the list
        count = nums.count(num)
        
        # Update max_count and max_num if the current count is higher
        if count > max_count:
            max_count = count
            max_num = num
    
    return max_num

# Test the function with the provided test case
assert max_occurrences([2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 2, 4, 6, 9, 1, 2]) == 2