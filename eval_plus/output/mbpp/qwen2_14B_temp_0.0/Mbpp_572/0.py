"""
Write a python function to remove duplicate numbers from a given number of lists.
assert two_unique_nums([1,2,3,2,3,4,5]) == [1, 4, 5]
"""
def two_unique_nums(nums):
    # Create a dictionary to count occurrences of each number
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    
    # Collect numbers that appear exactly twice
    result = []
    for num in nums:
        if counts[num] == 2:
            result.append(num)
    
    return result

# Test the function with the provided test case
assert two_unique_nums([1, 2, 3, 2, 3, 4, 5]) == [1, 4, 5]
