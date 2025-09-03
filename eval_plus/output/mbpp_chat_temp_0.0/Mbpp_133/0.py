"""
Write a function to calculate the sum of the negative numbers of a given list of numbers.
assert sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17])==-32
"""
def sum_negativenum(numbers):
    # Initialize the sum of negative numbers to zero
    neg_sum = 0
    
    # Iterate through each number in the list
    for num in numbers:
        # Check if the current number is negative
        if num < 0:
            # Add the negative number to the sum
            neg_sum += num
    
    # Return the total sum of negative numbers
    return neg_sum

# Test the function with the provided test case
assert sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17]) == -32
