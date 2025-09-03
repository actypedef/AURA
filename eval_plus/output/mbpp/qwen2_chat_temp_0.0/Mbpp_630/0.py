"""
Write a function to extract all the adjacent coordinates of the given coordinate tuple.
assert get_coordinates((3, 4)) == [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]]
"""
def get_coordinates(coord):
    # Extract x and y from the coordinate tuple
    x = coord[0]
    y = coord[1]
    
    # Initialize an empty list to store the result
    res = []
    
    # Iterate over possible x values (one less and one more than the current x)
    for i in range(x - 1, x + 2):
        # Iterate over possible y values (one less and one more than the current y)
        for j in range(y - 1, y + 2):
            # Check if the current point is not the same as the original point
            if i != x or j != y:
                # Append the point to the result list
                res.append([i, j])
    
    return res

# Test the function with the provided test case
assert get_coordinates((3, 4)) == [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]]