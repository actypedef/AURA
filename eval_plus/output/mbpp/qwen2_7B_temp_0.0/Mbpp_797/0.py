"""
Write a python function to find the sum of all odd natural numbers within the range l and r.
assert sum_in_range(2,5) == 8
"""
def sum_in_range(l, r):
    # Initialize the sum to zero
    sum = 0
    
    # Iterate through each number in the range from l to r (inclusive)
    for i in range(l, r + 1):
        # Check if the number is odd
        if i % 2 != 0:
            # Add the odd number to the sum
            sum += i
    
    # Return the total sum of odd numbers
    return sum

# Test the function with the provided test case
assert sum_in_range(2, 5) == 8
