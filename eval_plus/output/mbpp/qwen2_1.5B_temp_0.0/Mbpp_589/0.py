"""
Write a function to find perfect squares between two given numbers.
assert perfect_squares(1,30)==[1, 4, 9, 16, 25]
"""
def perfect_squares(start, end):
    # Initialize an empty list to store perfect squares
    squares = []
    
    # Loop through each number from start to end
    for num in range(start, end + 1):
        # Check if the square of the current number is within the range
        if num * num >= start and num * num <= end:
            # If so, add it to the list of squares
            squares.append(num * num)
    
    return squares

# Test the function with the provided test case
assert perfect_squares(1,30) == [1, 4, 9, 16, 25]