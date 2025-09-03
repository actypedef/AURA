import math

def max_fill(grid, capacity):
    """
    You are given a rectangular grid of wells. Each row represents a single well,
    and each 1 in a row represents a single unit of water.
    Each well has a corresponding bucket that can be used to extract water from it, 
    and all buckets have the same capacity.
    Your task is to use the buckets to empty the wells.
    Output the number of times you need to lower the buckets.

    Example 1:
        Input: 
            grid : [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
            bucket_capacity : 1
        Output: 6

    Example 2:
        Input: 
            grid : [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
            bucket_capacity : 2
        Output: 5
    
    Example 3:
        Input: 
            grid : [[0,0,0], [0,0,0]]
            bucket_capacity : 5
        Output: 0

    Constraints:
        * all wells have the same length
        * 1 <= grid.length <= 10^2
        * 1 <= grid[:,1].length <= 10^2
        * grid[i][j] -> 0 | 1
        * 1 <= capacity <= 10
    """
import math

def max_fill(grid, capacity):
    """
    You are given a rectangular grid of wells. Each row represents a single well,
    and each 1 in a row represents a single unit of water.
    Each well has a corresponding bucket that can be used to extract water from it, 
    and all buckets have the same capacity.
    Your task is to use the buckets to empty the wells.
    Output the number of times you need to lower the buckets.

    Example 1:
        Input: 
            grid : [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
            bucket_capacity : 1
        Output: 6

    Example 2:
        Input: 
            grid : [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
            bucket_capacity : 2
        Output: 5
    
    Example 3:
        Input: 
            grid : [[0,0,0], [0,0,0]]
            bucket_capacity : 5
        Output: 0

    Constraints:
        * all wells have the same length
        * 1 <= grid.length <= 10^2
        * 1 <= grid[:,1].length <= 10^2
        * grid[i][j] -> 0 | 1
        * 1 <= capacity <= 10
    """
    total_water = sum(sum(row) for row in grid)
    return math.ceil(total_water / capacity)

# Test cases
def test_max_fill():
    assert max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1) == 6
    assert max_fill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2) == 5
    assert max_fill([[0,0,0], [0,0,0]], 5) == 0
    assert max_fill([[1,1,1,1], [1,1,1,1]], 2) == 4
    assert max_fill([[1,1,1,1], [1,1,1,1], [1,1,1,1]], 3) == 4
    assert max_fill([[1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]], 4) == 4
    assert max_fill([[1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]], 5) == 4
    assert max_fill([[1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]], 6) == 4
    assert max_fill([[1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]], 7) == 4
    assert max_fill([[1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]], 8) == 4
    assert max_fill([[1