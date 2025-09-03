"""
Write a python function that takes in an integer n and finds the sum of the first n even natural numbers that are raised to the fifth power.
assert even_Power_Sum(2) == 1056
"""
def even_Power_Sum(n):
    # Initialize the sum to zero
    total_sum = 0
    
    # Loop through the first n even natural numbers
    for i in range(2, 2*n+1, 2):
        # Raise each number to the fifth power and add it to the total sum
        total_sum += i**5
    
    return total_sum

# Test cases to verify the correctness of the function
assert even_Power_Sum(2) == 1056
assert even_Power_Sum(3) == 4897
assert even_Power_Sum(4) == 129600
assert even_Power_Sum(5) == 302500