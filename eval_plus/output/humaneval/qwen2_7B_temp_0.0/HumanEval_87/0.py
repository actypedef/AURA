
def get_row(lst, x):
    """
    You are given a 2 dimensional data, as a nested lists,
    which is similar to matrix, however, unlike matrices,
    each row may contain a different number of columns.
    Given lst, and integer x, find integers x in the list,
    and return list of tuples, [(x1, y1), (x2, y2) ...] such that
    each tuple is a coordinate - (row, columns), starting with 0.
    Sort coordinates initially by rows in ascending order.
    Also, sort coordinates of the row by columns in descending order.
    
    Examples:
    get_row([
      [1,2,3,4,5,6],
      [1,2,3,4,1,6],
      [1,2,3,4,5,1]
    ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
    get_row([], 1) == []
    get_row([[], [1], [1, 2, 3]], 3) == [(2, 2)]
    """
def get_row(lst, x):
    """
    This function searches for all occurrences of an integer x in a 2D list
    and returns their coordinates sorted first by row in ascending order,
    then by column in descending order within each row.

    Args:
    lst: A 2D list where each sublist can have a varying number of elements.
    x: The integer to search for in the list.

    Returns:
    A list of tuples representing the coordinates of x in the format [(row, col)].
    """

    # Initialize an empty list to store the coordinates
    coordinates = []

    # Iterate over the list with index to get both row and column information
    for i, row in enumerate(lst):
        # Check if x is in the current row
        if x in row:
            # Find all indices of x in the current row
            for j in range(len(row)):
                if row[j] == x:
                    # Append the coordinate as a tuple (row, column)
                    coordinates.append((i, j))

    # Sort the coordinates by row in ascending order and then by column in descending order within each row
    coordinates.sort(key=lambda coord: (coord[0], -coord[1]))

    return coordinates

# Example usage: