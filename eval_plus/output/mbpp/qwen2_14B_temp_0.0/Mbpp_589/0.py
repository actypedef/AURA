"""
Write a function to find perfect squares between two given numbers.
assert perfect_squares(1,30)==[1, 4, 9, 16, 25]
"""
import math

def perfect_squares(start, end):
    # Initialize an empty list to store perfect squares
    squares = []
    
    # Loop through numbers from the square root of start to the square root of end
    for i in range(int(math.sqrt(start)), int(math.sqrt(end)) + 1):
        # Append the square of the current number to the list
        squares.append(i * i)
    
    return squares

# Test the function with the provided test case
assert perfect_squares(1, 30) == [1, 4, 9, 16, 25]
