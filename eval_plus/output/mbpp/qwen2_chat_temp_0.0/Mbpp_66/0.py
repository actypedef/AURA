"""
Write a python function to count the number of positive numbers in a list.
assert pos_count([1,-2,3,-4]) == 2
"""
def pos_count(nums):
    # Initialize a counter for positive numbers
    count = 0
    
    # Iterate through each number in the list
    for num in nums:
        # Check if the number is positive
        if num > 0:
            # Increment the counter if the number is positive
            count += 1
            
    # Return the total count of positive numbers
    return count

# Test the function with the provided test case
assert pos_count([1, -2, 3, -4]) == 2
