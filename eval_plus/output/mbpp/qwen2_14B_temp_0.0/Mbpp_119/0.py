"""
Write a python function to find the element that appears only once in a sorted array.
assert search([1,1,2,2,3]) == 3
"""
def search(nums):
    # Iterate through the array
    for i in range(0, len(nums), 2):
        # Check if the current element is the last one or different from the next element
        if (i == len(nums) - 1 or nums[i] != nums[i + 1]):
            return nums[i]

# Test the function with the provided test case
assert search([1, 1, 2, 2, 3]) == 3
