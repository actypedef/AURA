"""
Write a function to check whether a specified list is sorted or not.
assert issort_list([1,2,4,6,8,10,12,14,16,17])==True
"""
def issort_list(nums):
    # Check if the list is empty or contains only one element
    if len(nums) <= 1:
        return True
    
    # Iterate through the list and compare each element with the next one
    for i in range(len(nums) - 1):
        # If any element is greater than the next one, the list is not sorted
        if nums[i] > nums[i + 1]:
            return False
    
    # If no elements are out of order, the list is sorted
    return True

# Test the function with the provided test case
assert issort_list([1, 2, 4, 6, 8, 10, 12, 14, 16, 17]) == True