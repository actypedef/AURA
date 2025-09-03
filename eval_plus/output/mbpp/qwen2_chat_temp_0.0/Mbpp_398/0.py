"""
Write a function to compute the sum of digits of each number of a given list.
assert sum_of_digits([10,2,56])==14
"""
def sum_of_digits(nums):
    # Initialize a variable to store the total sum of digits
    total_sum = 0
    
    # Iterate through each number in the list
    for num in nums:
        # Convert the number to a string to iterate over its digits
        for digit in str(num):
            # Add the integer value of the digit to the total sum
            total_sum += int(digit)
    
    # Return the total sum of digits
    return total_sum

# Test the function with the provided test case
assert sum_of_digits([10, 2, 56]) == 14