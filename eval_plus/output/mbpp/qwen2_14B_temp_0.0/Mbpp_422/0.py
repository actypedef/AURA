"""
Write a python function to find the average of cubes of first n natural numbers.
assert find_Average_Of_Cube(2) == 4.5
"""
def find_Average_Of_Cube(n):
    # Calculate the sum of cubes of the first n natural numbers
    sum = 0
    for i in range(1, n + 1):
        sum += (i ** 3)
    
    # Calculate the average by dividing the sum by n
    avg = sum / n
    return avg

# Test the function with the provided test case
assert find_Average_Of_Cube(2) == 4.5
