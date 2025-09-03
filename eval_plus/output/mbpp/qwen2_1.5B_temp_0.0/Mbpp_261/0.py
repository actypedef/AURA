"""
Write a function that takes in two tuples and performs mathematical division operation element-wise across the given tuples.
assert division_elements((10, 4, 6, 9),(5, 2, 3, 3)) == (2, 2, 2, 3)
"""
def division_elements(tuple1, tuple2):
    # Check if both tuples have the same length
    assert len(tuple1) == len(tuple2), "Both tuples must have the same length"
    
    # Perform element-wise division
    result = tuple(x / y for x, y in zip(tuple1, tuple2))
    
    return result

# Test cases to verify the correctness of the solution
assert division_elements((10, 4, 6, 9),(5, 2, 3, 3)) == (2, 2, 2, 3)
assert division_elements((7, 8, 9, 10),(2, 3, 4, 5)) == (3.5, 2.6666666666666665, 2.25, 2.0)
assert division_elements((1, 1, 1, 1),(1, 1, 1, 1)) == (1, 1, 1, 1)