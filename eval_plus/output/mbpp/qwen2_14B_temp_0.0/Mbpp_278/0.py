"""
Write a function to find the number of elements that occurs before the tuple element in the given tuple.
assert count_first_elements((1, 5, 7, (4, 6), 10) ) == 3
"""
def count_first_elements(test_tup):
    # Iterate through the tuple to find the first tuple element
    for count, ele in enumerate(test_tup):
        # Check if the current element is a tuple
        if isinstance(ele, tuple):
            # Return the count of elements before the found tuple
            return count

# Test the function with the provided test case
assert count_first_elements((1, 5, 7, (4, 6), 10)) == 3
