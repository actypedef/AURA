"""
Write a function to find the union of the elements of two given tuples and output them in sorted order.
assert union_elements((3, 4, 5, 6),(5, 7, 4, 10) ) == (3, 4, 5, 6, 7, 10)
"""
def union_elements(tuple1, tuple2):
    # Convert tuples to sets to remove duplicates and then use set union
    result = sorted(set(tuple1) | set(tuple2))
    return result

# Test the function with provided data points
assert union_elements((3, 4, 5, 6), (5, 7, 4, 10)) == (3, 4, 5, 6, 7, 10)