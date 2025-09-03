"""
Write a function to calculate the sum of the negative numbers of a given list of numbers.
assert sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17])==-32
"""
def sum_negativenum(nums):
    # Initialize sum to zero
    total = 0
    
    # Iterate through each number in the list
    for num in nums:
        # Check if the number is negative
        if num < 0:
            # Add the negative number to the total sum
            total += num
    
    # Return the total sum of negative numbers
    return total

# Test the function with the provided test case
assert sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17]) == -32
