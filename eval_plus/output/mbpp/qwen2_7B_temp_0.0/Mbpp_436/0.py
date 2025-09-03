"""
Write a python function to return the negative numbers in a list.
assert neg_nos([-1,4,5,-6]) == [-1,-6]
"""
def neg_nos(nums):
    # Initialize an empty list to store negative numbers
    neg_nums = []
    
    # Iterate through each number in the input list
    for num in nums:
        # Check if the number is negative
        if num < 0:
            # If it is, append it to the neg_nums list
            neg_nums.append(num)
    
    # Return the list of negative numbers
    return neg_nums

# Test the function with the provided test case
assert neg_nos([-1, 4, 5, -6]) == [-1, -6]
