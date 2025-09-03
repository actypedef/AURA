"""
Write a function to extract all the adjacent coordinates of the given coordinate tuple.
assert get_coordinates((3, 4)) == [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]]
"""
def get_coordinates(coord):
    # Extract the x and y values from the input coordinate tuple
    x, y = coord
    
    # Generate a list of all adjacent coordinates
    return [[i, j] for i in range(x - 1, x + 2) for j in range(y - 1, y + 2)]

# Test the function with the provided test case
assert get_coordinates((3, 4)) == [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]]
