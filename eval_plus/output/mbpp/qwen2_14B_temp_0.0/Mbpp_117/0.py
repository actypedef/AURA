"""
Write a function to convert all possible convertible elements in a list of lists to floats.
assert list_to_float( [("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")] ) == [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)]
"""
def list_to_float(list1):
    # Convert each element in the sublists to float if possible
    result = [tuple(map(float, item)) for item in list1]
    return result

# Test the function with the provided test case
assert list_to_float([("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")]) == [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)]
