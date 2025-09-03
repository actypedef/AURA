"""
Write a function to find perfect squares between two given numbers.
assert perfect_squares(1,30)==[1, 4, 9, 16, 25]
"""
def perfect_squares(start, end):
    # Initialize an empty list to store perfect squares
    perfects = []
    
    # Iterate through the range from start to end (inclusive)
    for i in range(start, end + 1):
        # Check if the current number is a perfect square
        if int(i**0.5) ** 2 == i:
            # If it is, append it to the list of perfect squares
            perfects.append(i)
    
    # Return the list of perfect squares
    return perfects

# Test the function with the provided test case
assert perfect_squares(1, 30) == [1, 4, 9, 16, 25]
