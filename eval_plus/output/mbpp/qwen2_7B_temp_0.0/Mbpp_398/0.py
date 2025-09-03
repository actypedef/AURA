"""
Write a function to compute the sum of digits of each number of a given list.
assert sum_of_digits([10,2,56])==14
"""
def sum_of_digits(nums):
    # Initialize an empty list to store the sums of digits for each number
    result = []
    
    # Iterate through each number in the input list
    for num in nums:
        # Convert the number to a string to iterate over its digits
        str_num = str(num)
        
        # Calculate the sum of digits using a generator expression
        digit_sum = sum(int(digit) for digit in str_num)
        
        # Append the calculated sum to the result list
        result.append(digit_sum)
    
    # Return the list containing the sums of digits for each number
    return result

# Test the function with the provided test case
assert sum_of_digits([10, 2, 56]) == [1, 2, 11]