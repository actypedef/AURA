"""
Write a python function to find the sum of fourth power of first n odd natural numbers.
assert odd_num_sum(2) == 82
"""
def odd_num_sum(n):
    # Initialize the sum variable to store the result
    sum = 0
    
    # Loop through the first n odd numbers
    for i in range(1, n + 1):
        # Calculate the fourth power of the current odd number
        num = (2 * i - 1)
        # Add the fourth power to the sum
        sum += num ** 4
    
    # Return the total sum of the fourth powers
    return sum

# Test the function with the provided test case
assert odd_num_sum(2) == 82