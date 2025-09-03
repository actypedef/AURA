"""
Write a function to convert all possible convertible elements in a list of lists to floats.
assert list_to_float( [("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")] ) == [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)]
"""
def list_to_float(lst):
    # Convert each element in the list of lists to float where possible
    return [[float(i) for i in j] for j in lst]

# Test the function with the provided test case
assert list_to_float([("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")]) == [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)]
