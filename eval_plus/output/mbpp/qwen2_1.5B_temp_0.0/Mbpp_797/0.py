"""
Write a python function to find the sum of all odd natural numbers within the range l and r.
assert sum_in_range(2,5) == 8
"""
def sum_in_range(l, r):
    # Initialize sum variable
    total_sum = 0
    
    # Iterate through each number in the range from l to r (inclusive)
    for num in range(l, r + 1):
        # Check if the number is odd
        if num % 2 != 0:
            # Add the odd number to the total sum
            total_sum += num
            
    # Return the final sum
    return total_sum

# Test the function with provided data points
assert sum_in_range(2,5) == 8