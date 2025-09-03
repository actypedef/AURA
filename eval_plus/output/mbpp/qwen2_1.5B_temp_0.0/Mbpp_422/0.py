"""
Write a python function to find the average of cubes of first n natural numbers.
assert find_Average_Of_Cube(2) == 4.5
"""
def find_Average_Of_Cube(n):
    # Calculate the sum of cubes of first n natural numbers using formula (n*(n+1)*(2*n+1))/6
    total_sum = (n * (n + 1) * (2 * n + 1)) / 6
    
    # Calculate the average by dividing the total sum by n
    average = total_sum / n
    
    return average

# Test the function with provided data points
assert find_Average_Of_Cube(2) == 4.5