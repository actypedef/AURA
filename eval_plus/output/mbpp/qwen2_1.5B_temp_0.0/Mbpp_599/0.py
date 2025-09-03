"""
Write a function to find sum and average of first n natural numbers.
assert sum_average(10)==(55, 5.5)
"""
def sum_average(n):
    # Calculate the sum of first n natural numbers using formula
    total_sum = (n * (n + 1)) // 2
    
    # Calculate the average of first n natural numbers
    average = total_sum / n
    
    return total_sum, average

# Test the function with provided data points
assert sum_average(10) == (55, 5.5)