"""
Write a function to find sum and average of first n natural numbers.
assert sum_average(10)==(55, 5.5)
"""
def sum_average(n):
    # Calculate the sum of the first n natural numbers using the formula for the sum of an arithmetic series
    total_sum = int(n * (n + 1) / 2)
    
    # Calculate the average of the first n natural numbers
    average = total_sum / n
    
    # Return both the sum and the average as a tuple
    return (total_sum, average)

# Test the function with the provided test case
assert sum_average(10) == (55, 5.5)
