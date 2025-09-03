"""
Write a function to find perfect squares between two given numbers.
assert perfect_squares(1,30)==[1, 4, 9, 16, 25]
"""
def perfect_squares(start, end):
    # Initialize an empty list to store perfect squares
    res = []
    
    # Iterate through the range from start to end (inclusive)
    for i in range(start, end + 1):
        # Check if the square root of the number is an integer
        if int(i ** 0.5) ** 2 == i:
            # If it is, append the number to the result list
            res.append(i)
    
    # Return the list of perfect squares
    return res

# Test the function with the provided test case
assert perfect_squares(1, 30) == [1, 4, 9, 16, 25]