"""
Write a python function to find the average of cubes of first n natural numbers.
assert find_Average_Of_Cube(2) == 4.5
"""
def find_Average_Of_Cube(n):
    # Initialize sum to store the sum of cubes
    sum = 0
    
    # Loop through the first n natural numbers
    for i in range(1, n + 1):
        # Calculate cube of each number and add it to sum
        sum += i ** 3
    
    # Calculate the average of cubes
    avg = sum / n
    
    return avg

# Test the function with the provided test case
assert find_Average_Of_Cube(2) == 4.5
