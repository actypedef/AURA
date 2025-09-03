"""
Write a function to extract all the adjacent coordinates of the given coordinate tuple.
assert get_coordinates((3, 4)) == [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]]
"""
def get_coordinates(coord):
    """
    Extracts all the adjacent coordinates of the given coordinate tuple.

    Args:
    coord (tuple): A tuple representing a coordinate (x, y).

    Returns:
    list: A list of tuples representing all adjacent coordinates.
    """
    x, y = coord
    return [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

# Test cases to verify the correctness of the solution
assert get_coordinates((3, 4)) == [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]]
assert get_coordinates((0, 0)) == [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
assert get_coordinates((1, 1)) == [[0, 0], [0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1], [2, 2]]