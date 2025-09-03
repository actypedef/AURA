"""
Write a python function that takes in an integer n and returns the sum of the squares of the first n odd natural numbers.
assert square_Sum(2) == 10
"""
def square_Sum(n):
    # Initialize the sum to zero
    total_sum = 0
    
    # Loop through the first n odd natural numbers
    for i in range(1, 2*n, 2):
        # Add the square of each number to the total sum
        total_sum += i**2
    
    return total_sum

# Test cases to verify the correctness of the function
assert square_Sum(2) == 10
assert square_Sum(3) == 35
assert square_Sum(4) == 84
assert square_Sum(5) == 165