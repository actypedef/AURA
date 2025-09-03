"""
Write a function to check if each element of second tuple is smaller than its corresponding element in the first tuple.
assert check_smaller((1, 2, 3), (2, 3, 4)) == False
"""
def check_smaller(tup1, tup2):
    # Check if all elements in the second tuple are less than their corresponding elements in the first tuple
    return all(x < y for x, y in zip(tup1, tup2))

# Test cases to verify the correctness of the function
assert check_smaller((1, 2, 3), (2, 3, 4)) == False
assert check_smaller((5, 6, 7), (5, 6, 8)) == True
assert check_smaller((0, 0, 0), (0, 0, 0)) == True
assert check_smaller((-1, -2, -3), (-2, -3, -4)) == True
assert check_smaller((10, 20, 30), (10, 20, 30)) == True
assert check_smaller((100, 200, 300), (100, 200, 301)) == False