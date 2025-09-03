"""
Write a function to extract all the adjacent coordinates of the given coordinate tuple.
assert get_coordinates((3, 4)) == [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]]
"""
def get_coordinates(test_tup):
    # Extract x and y coordinates from the input tuple
    x, y = test_tup
    
    # Generate all possible adjacent coordinates using list comprehension
    res = [[x + i, y + j] for i in range(-1, 2) for j in range(-1, 2)]
    
    return res

# Test the function with the provided test case
assert get_coordinates((3, 4)) == [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]]
